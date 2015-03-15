# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('source_pages', '0008_auto_20150315_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_name', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=64, blank=True)),
                ('last_modified', models.CharField(max_length=32, blank=True)),
                ('scraped_href', models.CharField(max_length=200)),
                ('absolute_url', models.CharField(max_length=300)),
                ('current_etag', models.CharField(max_length=32, null=True, blank=True)),
                ('previous_etag', models.CharField(max_length=32, null=True, blank=True)),
                ('timestamp', models.DateTimeField(verbose_name=b'date added')),
                ('last_run', models.DateTimeField(null=True, blank=True)),
                ('status_code', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('source_page', models.ForeignKey(to='source_pages.SourcePage')),
            ],
            options={
                'ordering': ('source_page', 'file_name'),
            },
            bases=(models.Model,),
        ),
    ]
