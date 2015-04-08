# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_auto_20150318_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='current_sha256',
            field=models.CharField(default=b'', max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='form',
            name='previous_sha256',
            field=models.CharField(default=b'', max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
