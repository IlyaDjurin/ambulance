from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Doctor, Reception
from .forms import ReceptionForm
from datetime import datetime, date, time
from django.template import RequestContext

class DoctorList(ListView):
    model = Doctor
    template_name='start.html'
    context_object_name = 'doctors'

class ReceptionView(FormView):
    form_class = ReceptionForm
    template_name = 'reception.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kwargs = None

    def form_valid(self, form):
        fcd = form.cleaned_data
        curr_doctor=Doctor.objects.get(id= self.kwargs['doctor_id'])
        response_dict={"form":form,
                       "doctor":curr_doctor,
                       "curr_date":fcd['date'],
                       "curr_time":fcd['time']}
        d = fcd['date']
        d1 = datetime.isoweekday(d)
        print(d1)
        t = fcd['time']
        t1 = time(9, 00)
        t2 = time(17, 00)
        # условие для предотвращения записи на один и тот же день,на то же время
        #  или выходной день у данного врача
        if Reception.objects.filter(date=fcd['date'],time=fcd['time'],doctor=curr_doctor).count()==0 and 1<=d1<=5 and t1<=t<=t2:


            Reception.objects.create(date=fcd['date'],time=fcd['time'],
                                     patient_name=fcd['patient_name'],
                                     patient_info=fcd['patient_info'],
                                     doctor=curr_doctor)
            response_dict["norm"] = "Вы записаны на прием"
            return render_to_response('reception.html', response_dict,)
        else:
            response_dict["message"]="Это время уже занято,или вы пытаетесь записаться в не рабочее время или выходной день." \
                                     " Пожалуйста выберите другое время или дату"
            return render_to_response('reception.html',response_dict,
                          )

    def get_context_data(self, **kwargs):
        context = super(ReceptionView, self).get_context_data(**kwargs)
        context['doctor']=Doctor.objects.get(id= self.kwargs['doctor_id'])
        return context
