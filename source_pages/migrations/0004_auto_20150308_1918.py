# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('source_pages', '0003_auto_20150308_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourcepage',
            name='previous_site_url',
            field=models.CharField(max_length=300, verbose_name=b'previous site url', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourcepage',
            name='scraper_filename',
            field=models.CharField(max_length=32, verbose_name=b'scraper filename', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourcepage',
            name='site_title',
            field=models.CharField(max_length=300, verbose_name=b'site title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourcepage',
            name='site_url',
            field=models.CharField(max_length=300, verbose_name=b'site url'),
            preserve_default=True,
        ),
    ]
