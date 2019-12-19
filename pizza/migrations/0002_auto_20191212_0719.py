from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizza',
            options={'verbose_name_plural': 'pizze'},
        ),
        migrations.AlterModelOptions(
            name='skladnik',
            options={'verbose_name_plural': 'skladniki'},
        ),
        migrations.RenameField(
            model_name='skladnik',
            old_name='pizze',
            new_name='pizza',
        ),
    ]