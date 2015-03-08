# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SourcePage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_title', models.CharField(max_length=200, verbose_name=b'site title')),
                ('site_url', models.CharField(max_length=200, verbose_name=b'site url')),
                ('timestamp', models.DateTimeField(verbose_name=b'date added')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
