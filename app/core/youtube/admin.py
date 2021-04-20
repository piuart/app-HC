from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from core.youtube.models import *

# Register your models here.
admin.site.register(Channel)
admin.site.register(Video)
admin.site.register(Category)
#admin.site.register(AdminSite)