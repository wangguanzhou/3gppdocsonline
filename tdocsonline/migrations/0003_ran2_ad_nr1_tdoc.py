# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tdocsonline', '0002_auto_20170116_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='RAN2_AD_NR1_Tdoc',
            fields=[
                ('tdoc_number', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('tdoc_title', models.CharField(max_length=120)),
                ('tdoc_source', models.CharField(max_length=60)),
                ('tdoc_type', models.CharField(max_length=10)),
                ('tdoc_agendaitem', models.CharField(max_length=10)),
                ('tdoc_ai_description', models.CharField(max_length=40)),
                ('tdoc_status', models.CharField(max_length=10)),
                ('tdoc_revision_of', models.CharField(max_length=10)),
                ('tdoc_revised_to', models.CharField(max_length=10)),
                ('tdoc_release', models.CharField(max_length=10)),
                ('tdoc_workitem', models.CharField(max_length=16)),
            ],
        ),
    ]