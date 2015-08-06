import sys

import requests

from source_pages.models import SourcePage


class PageRequest:

    '''This class contains the method for making the initial
    request for the pages that contain the form links. The
    purpose is to determine if the pages have valid url's.

    The run script will run the method: update_page_request_data.
    The source page's status code or error message will be saved
    to the database.

    Please see the README.md for instructions on running this script.
    '''

    def __init__(self):
        # self.pages = SourcePage.objects.exclude(notes='discontinue')
        self.pages = SourcePage.objects.filter(status_code=None) 


    def update_page_request_data(self):        
        for page in self.pages:
            response = self._request_source_page(page)
            page.status_code = response['status_code']
            page.error_message = response['error_message']
            page.save()

    def _request_source_page(self, page):
        try:
            response = requests.get(page.site_url, timeout=30, verify=False)
            print(response.status_code, page.site_url)
            return {'status_code': response.status_code,
                    'error_message': ''}
        
        except:
            print(page.site_url, str(sys.exc_info()[0]))
            return {'status_code': None,
                    'error_message': str(sys.exc_info()[0])}


def run():
    page_request = PageRequest()
    page_request.update_page_request_data()
