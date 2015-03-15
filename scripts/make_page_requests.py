from source_pages.models import SourcePage

import requests

class PageRequests:
    def __init__(self):
        self.pages = SourcePage.objects.all() 

    def update_page_request_data(self):        
        for page in self.pages:
            response = self.request_source_page(page)
            page.status_code = response['status_code']
            page.error_message = response['error_message']
            page.save()

    def request_source_page(self, page):
        try:
            response = requests.head(page.site_url)
            print response.status_code, page.site_url
            return {'status_code': response.status_code,
                    'error_message': ''}
        
        except BaseException, e:
            print page.site_url, e
            return {'status_code': None,
                    'error_message': e}

    def write_to_csv(self):
        pass

def run():
    pr = PageRequests()
    pr.update_page_request_data()
