from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User,on_delete = models.CASCADE)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username



DIRECTION_OPTIONS = (
    ('horizantal','HORIZANTAL'),
    ('vertical','VERTICAL'),
)


class ServiceInfo(models.Model):

    auto_project_id = models.AutoField(primary_key = True) 
    servicename = models.CharField(max_length=64)
    communication_text = models.CharField(max_length=64)
    things_text = models.CharField(max_length=64)
    child = models.CharField(max_length=64)
    parent = models.CharField(max_length=64)
    
    direction = models.CharField(max_length=12, choices = DIRECTION_OPTIONS)


    def __str__(self):

        return str(self.auto_project_id)




# class DirectionInfo(models.Model):

#     direction = models.CharField(max_length=12, choices = DIRECTION_OPTIONS)
#     child = models.CharField(max_length=64)
#     parent = models.CharField(max_length=64)

#     def __str__(self):

#         return self.child





