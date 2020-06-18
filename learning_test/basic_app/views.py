from django.shortcuts import render, redirect
from basic_app.forms import (
    UserForm,
    UserProfileInfoForm,
    ServiceForm,
    )
from basic_app.models import (
    UserProfileInfo,
    ServiceInfo,
    )
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    update_session_auth_hash
    )


from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
# from pip import django-searchbar
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.

def index(request):
    return render(request, 'basic_app/index.html' )

@login_required
def special(request):
    return HttpResponse("you arer logging in")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'basic_app/profile.html', args)

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'basic_app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return render(request,'basic_app/projectpage.html')
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'basic_app/login.html', {})



# def projectpage(request):

#     return HttpResponseRedirect(reverse('index'))

def service(request):

    formfilled = False
    # form = ServiceForm()

    if request.method == 'POST':

        service_form = ServiceForm(data = request.POST)
        # diretion_form = DirectionForm(data = request.POST)

        if service_form.is_valid():

            service = service_form.save()
            # direction = diretion_form.save()

            service.save()
            # direction.save()


            formfilled = True

        else:
            print(service_form.errors)

    else:

        service_form = ServiceForm()
        # diretion_form = DirectionForm()

    return render(request, 'basic_app/serviceform.html',
                            {
                                'service_form' : service_form,
                                'formfilled' :formfilled
                            })


def exist(request):

    service_exist = ServiceInfo.objects.order_by('auto_project_id')
    service_dict = {'servicename' : service_exist }

    return render(request, 'basic_app/output.html',context=service_dict)

def search(request):
    if request.method == "POST":
        servicename = request.POST['servicename']

        if servicename:
            service_match = ServiceInfo.objects.filter(Q(servicename__istartswith = servicename))


            if service_match:
                return render(request, 'basic_app/search.html',{'servicematch' :service_match})
            else:
                messages.error(request,'noresult')
        else:
            return HttpResponseRedirect('basic_app/search/')

    return render(request, 'basic_app/search.html' )




# def my_view(request):
#     search_bar = SearchBar(request, ['name', 'age'])

#     #When the form is coming from posted page
#     if search_bar.is_valid():
#         my_name = search_bar['name']
#         ServiceInfo.objects.filter(name__contains=my_name)


def change_password(request):
    if request.method == 'POST':
        changeform = PasswordChangeForm(data =request.POST, user = request.user)

        if changeform.is_valid():
            changeform.save()
            # update_session_auth_hash(request, changeform.user)

            return redirect('index')
        else:

            return HttpResponse("Invalid login details supplied.")


        
    else:
        changeform = PasswordChangeForm(user = request.user)

        # args = {'changeform' : changeform}
        return render(request, 'basic_app/change_password.html', {'changeform' : changeform}) 




        