from django.db import models

from source_pages.models import SourcePage


class Form(models.Model):
    file_name = models.CharField(max_length=200)
    name = models.CharField(max_length=64, blank=True)
    source_page = models.ForeignKey(SourcePage)
    last_modified = models.CharField(max_length=32, blank=True)
    scraped_href = models.CharField(max_length=200)
    absolute_url = models.CharField(max_length=300)
    current_etag = models.CharField(max_length=32, null=True, blank=True)
    previous_etag = models.CharField(max_length=32, null=True, blank=True)
    timestamp = models.DateTimeField('date added')
    last_run = models.DateTimeField(null=True, blank=True)
    status_code = models.PositiveSmallIntegerField(null=True, blank=True)
    ignore = models.BooleanField(default=False)
    notes = models.TextField(blank=True)


    def __unicode__(self):
        return self.file_name

    class Meta:
        ordering = ('source_page', 'file_name',)