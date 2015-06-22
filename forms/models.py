from django.db import models

from source_pages.models import SourcePage


class Form(models.Model):
    file_name = models.CharField(max_length=200)
    name = models.CharField(max_length=64, blank=True)
    source_page = models.ForeignKey(SourcePage)
    last_modified = models.CharField(max_length=32, blank=True)
    canonical_url = models.CharField(max_length=300)
    current_etag = models.CharField(max_length=128, blank=True, default='')
    previous_etag = models.CharField(max_length=128, blank=True, default='')
    current_sha256 = models.CharField(max_length=128, blank=True, default='')
    previous_sha256 = models.CharField(max_length=128, blank=True, default='')
    timestamp = models.DateTimeField('date added')
    last_run = models.DateTimeField(null=True, blank=True)
    status_code = models.PositiveSmallIntegerField(null=True, blank=True)
    ignore = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    last_run_index = models.PositiveSmallIntegerField(null=True, blank=True)
    form_numbers = models.CharField(max_length=128, blank=True, default='')


    def __str__(self):
        return self.file_name

    class Meta:
        ordering = ('source_page', 'file_name',)


class Hash(models.Model):
    sha256 = models.CharField(max_length=128)
    last_run = models.DateTimeField('last run')
    form = models.ForeignKey(Form)
    last_run_index = models.PositiveSmallIntegerField(null=True, blank=True)


    def __str__(self):
        return self.sha256

    class Meta:
        ordering = ('last_run',)
