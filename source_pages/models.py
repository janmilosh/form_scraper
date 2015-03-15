from django.db import models


class SourcePage(models.Model):
    site_title = models.CharField('site title', max_length=300)
    site_url = models.CharField('site url', max_length=300)
    previous_site_url = models.CharField('previous site url', max_length=300,
                                                              blank=True)
    base_url = models.CharField('base url', max_length = 128,
                                            blank=True)
    timestamp = models.DateTimeField('date added')
    status_code = models.PositiveSmallIntegerField(null=True, blank=True)
    error_message = models.TextField(blank=True)
    notes = models.TextField(blank=True)


    def __unicode__(self):
        return self.site_title

    class Meta:
        ordering = ('site_title',)