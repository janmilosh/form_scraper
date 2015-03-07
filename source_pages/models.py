from django.db import models


class SourcePage(models.Model):
    site_title = models.CharField('site title', max_length=200)
    site_url = models.CharField('site url', max_length=200)
    timestamp = models.DateTimeField('date added')
