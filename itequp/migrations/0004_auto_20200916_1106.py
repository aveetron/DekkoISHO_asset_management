# Generated by Django 2.2 on 2020-09-16 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itequp', '0003_allocatedevice_assign_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocatedevice',
            name='assign_date',
            field=models.DateField(),
        ),
    ]
