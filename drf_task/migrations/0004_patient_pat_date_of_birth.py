# Generated by Django 4.1.7 on 2023-03-17 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_task', '0003_remove_hospital_hos_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='pat_date_of_birth',
            field=models.DateField(default='1998-12-12'),
            preserve_default=False,
        ),
    ]
