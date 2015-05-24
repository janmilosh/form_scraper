# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0009_auto_20150522_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='form_numbers',
            field=models.CharField(default=b'', max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
