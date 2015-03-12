# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('source_pages', '0005_auto_20150310_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourcepage',
            name='error_message',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourcepage',
            name='status_code',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourcepage',
            name='base_url',
            field=models.CharField(max_length=128, verbose_name=b'base url', blank=True),
            preserve_default=True,
        ),
    ]
