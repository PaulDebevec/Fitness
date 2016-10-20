# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 02:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbmiprofile',
            name='human_weight',
            field=models.FloatField(help_text='Enter weight in pounds'),
        ),
        migrations.AlterField(
            model_name='userweight',
            name='user_weight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.UserBMIProfile'),
        ),
    ]
