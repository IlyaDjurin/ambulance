# coding: utf-8
from django import forms
from .models import Doctor, Reception
from django.contrib.admin import widgets
import datetime

class ReceptionForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = ['date','time','patient_name','patient_info']

    def __init__(self, *args, **kwargs):
        super(ReceptionForm, self).__init__(*args, **kwargs)

        self.fields['patient_info'].widget = forms.Textarea(attrs={'cols': 60, 'rows': 8})
        self.fields['patient_info'].label = 'Что вас беспокоит'





