from django.conf.urls import url
from basic_app import views
from django.contrib.auth import views as auth_views


# SET THE NAMESPACE!
app_name = 'basic_app'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    # url(r'^projectspage', views.projectpage,name='projectpage'),
    url(r'^service/$', views.service, name ="service"),
    url(r'^exist/$', views.exist, name = 'exist'),
    url(r'search/$', views.search,name = "search"),
    url(r'change_password/$', views.change_password,name = "change_password"),


]
