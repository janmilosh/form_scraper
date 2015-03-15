# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('source_pages', '0007_sourcepage_notes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sourcepage',
            options={'ordering': ('site_title',)},
        ),
    ]
