from django.db import models


class SourcePage(models.Model):
    site_title = models.CharField('site title', max_length=300)
    site_url = models.CharField('site url', max_length=300)
    previous_site_url = models.CharField('previous site url',
                                         max_length=300,
                                         blank=True)
    scraper_filename = models.CharField('scraper filename',
                                        max_length = 32,
                                        blank=True)
    timestamp = models.DateTimeField('date added')


    def __unicode__(self):
        return self.site_title