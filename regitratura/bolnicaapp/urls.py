from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^doctor/(?P<doctor_id>\d+)/contact$',views.ReceptionView, name='contact'),

    ]

