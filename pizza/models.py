from django.db import models

# Create your models here.
class Pizza(models.Model):
    LARGE = 'L'
    MEDIUM = 'M'
    SMALL = 'S'
    ROZMIARY = (
        (LARGE, 'przełogromna'),
        (MEDIUM, 'średnia'),
        (SMALL, 'malusieńka'),
    )

    nazwa = models.CharField(verbose_name='pizza', max_length=30)
    opis = models.TextField(blank=True, help_text='Opis pizzy')
    rozmiar = models.CharField(max_length=1, choices=ROZMIARY, default=LARGE)
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField('dodano',auto_now_add=True)

class Skladnik(models.Model):
    pizza = models.ForeignKey(Pizza,
                                on_delete=models.CASCADE,
                                related_name='skladniki')
    nazwa = models.CharField(verbose_name='skladnik', max_length=30)
    jarski = models.BooleanField(
        verbose_name='jarski?',
        help_text='Zaznacz jeżeli ci odpowiada',
        default=False)
