# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('userpassword', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
