from django.contrib import admin
from basic_app.models import UserProfileInfo, ServiceInfo

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(ServiceInfo)