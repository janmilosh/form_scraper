from django.db import models

import requests


class SourcePage(models.Model):
    site_title = models.CharField('site title', max_length=300)
    site_url = models.CharField('site url', max_length=300)
    previous_site_url = models.CharField('previous site url',
                                         max_length=300,
                                         blank=True)
    base_url = models.CharField('base url',
                                        max_length = 128,
                                        blank=True)
    timestamp = models.DateTimeField('date added')
    status_code = models.PositiveSmallIntegerField(null=True, blank=True)
    error_message = models.TextField(blank=True)


    def request_source_page(self):
        try:
            response = requests.get(self.site_url)
            print response.status_code, self.site_title
            print self.site_url
            print
            return {'status_code': response.status_code,
                    'error_message': ''}
        
        except BaseException, e:
            print e
            print self.site_title
            print self.site_url
            print
            return {'status_code': None,
                    'error_message': e}


    def __unicode__(self):
        return self.site_title