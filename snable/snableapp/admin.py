from django.contrib import admin
from .models import ProfileModel

# Register your models here.

class PersonalAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','email']

admin.site.register(ProfileModel,PersonalAdmin)