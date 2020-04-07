# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-03 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin', '0050_update_userprofile_timezone_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='sharpen_thumbnails',
            field=models.BooleanField(
                default=False,
                help_text="If selected, AstroBin will use a resizing algorithm that slightly sharpens the image's "
                          "thumbnails. This setting applies to all revisions.",
                verbose_name='Sharpen thumbnails'),
        ),
    ]