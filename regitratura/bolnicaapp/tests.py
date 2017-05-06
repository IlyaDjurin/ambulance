from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from bolnicaapp.models import Doctor, Reception
from datetime import datetime, date, time



# Create your tests here.



class DoctorModelTest(TestCase):
    def test_verbose_name_plural(self):
        self.assertEqual(str(Doctor._meta.verbose_name_plural), "Врачи")

    def test_verbose_name(self):
        self.assertEqual(str(Doctor._meta.verbose_name), "Врач")

    def test_doc_database(self):
        Doctor.objects.create(name="Тимченко Сергей", specialization="Стоматолог", info="Лечит зубы")
        doc = Doctor.objects.get(specialization="Стоматолог")
        self.assertEqual(str(doc.name), "Тимченко Сергей")


class ReceptionModelTest(TestCase):
    def test_verbose_name_plural(self):
        self.assertEqual(str(Reception._meta.verbose_name_plural), "Приемы")

    def test_verbose_name(self):
        self.assertEqual(str(Reception._meta.verbose_name), "Прием")

    def test_reception_database(self):
        d = Doctor.objects.create(name="Тимченко Сергей", specialization="Стоматолог", info="Лечит зубы")

        Reception.objects.create(date=date(2017, 5, 6), time=time(9, 00),
                                 patient_name="Вася",
                                 patient_info="У Васи болит зуб",
                                 doctor=d)
        rec = Reception.objects.get(id=1)
        self.assertEqual(str(rec.patient_name), "Вася")


class ViewsTest(TestCase):
    def test_call_view_loads(self):

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_call_view_admin(self):

        response = self.client.get('/http://127.0.0.1:8000/admin/')

        self.assertEqual(response.status_code, 200)


