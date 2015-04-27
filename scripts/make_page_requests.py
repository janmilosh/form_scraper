from source_pages.models import SourcePage

import requests


class PageRequest:
    def __init__(self):
        self.pages = SourcePage.objects.all() 

    def update_page_request_data(self):        
        for page in self.pages:
            if page.status_code != 200:
                response = self._request_source_page(page)
                page.status_code = response['status_code']
                page.error_message = response['error_message']
                page.save()

    def _request_source_page(self, page):
        try:
            response = requests.get(page.site_url)
            print response.status_code, page.site_url
            return {'status_code': response.status_code,
                    'error_message': ''}
        
        except BaseException, e:
            print page.site_url, e
            return {'status_code': None,
                    'error_message': e}


def run():
    page_request = PageRequest()
    page_request.update_page_request_data()
