from django.contrib import admin

# Register your models here.

from app01 import models

admin.site.register(models.Userinfo)
admin.site.register(models.Room)
admin.site.register(models.Relationship)