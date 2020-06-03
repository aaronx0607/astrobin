# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-02 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RemoteSourceAffiliate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('code', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=256)),
                ('affiliation_start', models.DateTimeField(null=True, blank=True)),
                ('affiliation_expiration', models.DateField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
