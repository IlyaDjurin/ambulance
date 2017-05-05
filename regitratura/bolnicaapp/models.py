from django.db import models

# Create your models here.

class Doctor (models.Model):
    name=models.CharField(verbose_name='ФИО врача', max_length = 200 )
    specialization=models.CharField(verbose_name='Специальность',max_length=200)
    info=models.TextField(verbose_name='Информация о враче')

    def __str__(self):
        return '%s ' % self.name

    class Meta:
        verbose_name_plural = "Врачи"
        verbose_name = "Врач"


class Reception(models.Model):
    date = models.DateField(verbose_name='Дата приема ')
    time=models.TimeField(verbose_name='Время приема ')
    patient_name=models.CharField(verbose_name='ФИО пациента', max_length=200)
    patient_info=models.TextField(verbose_name='Информация о пациенте ')
    doctor=models.ForeignKey( Doctor, verbose_name='Лечащий врач ',)

    def __str__(self):
        return 'Прием № %s' % self.id

    class Meta:
        verbose_name_plural = "Приемы"
        verbose_name = "Прием"
