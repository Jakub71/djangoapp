# Generated by Django 2.2.6 on 2019-12-19 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_auto_20191212_0719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skladnik',
            name='pizza',
        ),
        migrations.AddField(
            model_name='skladnik',
            name='pizze',
            field=models.ManyToManyField(related_name='skladniki', to='pizza.Pizza'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='cena',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='opis',
            field=models.TextField(blank=True, default='', help_text='Opis pizzy'),
        ),
    ]
