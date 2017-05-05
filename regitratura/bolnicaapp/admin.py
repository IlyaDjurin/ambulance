from django.contrib import admin

# Register your models here.

from django.forms import ModelForm
from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from .models import Doctor, Reception



class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization','info']

class ReceptionAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'patient_info','doctor','date','time']


admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Reception,ReceptionAdmin)

