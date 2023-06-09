# Generated by Django 4.1.7 on 2023-03-16 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('length', models.IntegerField()),
                ('rental_duration', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
