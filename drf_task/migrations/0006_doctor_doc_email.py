# Generated by Django 4.1.7 on 2023-03-20 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_task', '0005_alter_patient_pat_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='doc_email',
            field=models.CharField(default='admin@gmail.com', max_length=255),
            preserve_default=False,
        ),
    ]
