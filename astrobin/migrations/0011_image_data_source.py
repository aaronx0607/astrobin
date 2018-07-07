# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-10 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin', '0010_image_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='data_source',
            field=models.CharField(choices=[(None, b'---------'), ('Self acquired', ((b'BACKYARD', 'Backyard'), (b'TRAVELLER', 'Traveller'), (b'OWN_REMOTE', 'Own remote observatory'))), ('Downloaded', ((b'AMATEUR_HOSTING', 'Amateur hosting facility'), (b'PUBLIC_AMATEUR_DATA', 'Public amateur data'), (b'PRO_DATA', 'Professional, scientific grade data'))), ('Other', ((b'MIX', 'Mix of multiple sources'), (b'OTHER', 'None of the above'), (b'UNKNOWN', 'Unknown')))], default=b'UNKNOWN', help_text='Where does the data for this image come from?', max_length=32, verbose_name='Data source'),
        ),
    ]