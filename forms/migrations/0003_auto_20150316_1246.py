# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_form_ignore'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='absolute_url',
            new_name='canonical_url',
        ),
        migrations.RemoveField(
            model_name='form',
            name='scraped_href',
        ),
    ]
