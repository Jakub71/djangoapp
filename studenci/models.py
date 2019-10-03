from django.db import models

class Miasto(models.Model):
    nazwa = models.CharField(verbose_name='miasto', max_length=30, help_text='Nazwa miasta')
    kod = models.CharField(max_length=6, help_text='Kod pocztowy')

class Uczelnia(models.Model):
    nazwa = models.CharField(verbose_name='uczelnia', max_length=60, help_text='Nazwa uczelni')

class Student(models.Model):
    imie = models.CharField(verbose_name='imię', max_length=30)
    nazwisko = models.CharField(max_length=30)
    miasto = models.ForeignKey(Miasto, on_delete=models.SET_NULL, null=True)
    uczelnia =  models.ForeignKey(Uczelnia, on_delete=models.DO_NOTHING, null=True)
    roks = models.CharField(verbose_name='rok studiów', max_length=3)
    dochod = models.DecimalField(max_digits='6',decimal_places=2)