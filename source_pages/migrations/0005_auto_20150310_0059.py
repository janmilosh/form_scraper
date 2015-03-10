# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('source_pages', '0004_auto_20150308_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sourcepage',
            name='scraper_filename',
        ),
        migrations.AddField(
            model_name='sourcepage',
            name='base_url',
            field=models.CharField(max_length=128, verbose_name=b'scraper filename', blank=True),
            preserve_default=True,
        ),
    ]
