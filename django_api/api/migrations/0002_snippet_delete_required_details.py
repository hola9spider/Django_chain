# Generated by Django 4.1.5 on 2023-04-21 05:23

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, default='', max_length=25)),
                ('Email_ID', models.CharField(max_length=35)),
                ('Phone_number', models.CharField(max_length=12)),
                ('Subject', models.CharField(max_length=20)),
                ('Categories', models.CharField(choices=[('Category1', 'Car'), ('Category2', 'Bike'), ('Category3', 'Furniture')], default='Car', max_length=10, verbose_name=django.contrib.auth.models.User)),
                ('Description', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['Name'],
            },
        ),
        migrations.DeleteModel(
            name='Required_details',
        ),
    ]