# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('source_pages', '0006_auto_20150312_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourcepage',
            name='notes',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
