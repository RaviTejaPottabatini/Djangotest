from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo,ServiceInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')



class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')


class ServiceForm(forms.ModelForm):

    communication_text = forms.CharField()
    things_text = forms.CharField()
    child = forms.CharField()
    parent = forms.CharField()

    class Meta():
        model = ServiceInfo
        fields = ('servicename', 'communication_text', 'things_text','direction', 'child', 'parent')


# class DirectionForm(forms.ModelForm):

#     # direction = forms.CharField()

#     class Meta():
#         model = DirectionInfo
#         fields = ('direction', 'child', 'parent')




