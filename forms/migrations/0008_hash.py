# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_auto_20150408_0225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hash',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sha256', models.CharField(max_length=128)),
                ('last_run', models.DateTimeField(verbose_name=b'last run')),
                ('form', models.ForeignKey(to='forms.Form')),
            ],
            options={
                'ordering': ('last_run',),
            },
            bases=(models.Model,),
        ),
    ]
