# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20150316_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='current_etag',
            field=models.CharField(default=b'', max_length=32, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='form',
            name='previous_etag',
            field=models.CharField(default=b'', max_length=32, blank=True),
            preserve_default=True,
        ),
    ]
