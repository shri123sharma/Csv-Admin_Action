# Generated by Django 4.1.7 on 2023-03-17 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drf_task', '0002_hospital_hos_pincode_patient_pat_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='Hos_pincode',
        ),
    ]
