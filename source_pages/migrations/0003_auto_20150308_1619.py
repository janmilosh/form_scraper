# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('source_pages', '0002_auto_20150308_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourcepage',
            name='site_title',
            field=models.CharField(max_length=500, verbose_name=b'site title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourcepage',
            name='site_url',
            field=models.CharField(max_length=500, verbose_name=b'site url'),
            preserve_default=True,
        ),
    ]
