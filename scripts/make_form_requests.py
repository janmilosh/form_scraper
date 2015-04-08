import requests, pdb

from forms.models import Form
from helpers.pdf_scrape import Helpers


class FormRequest:
    def __init__(self):
        self.forms = Form.objects.all()
        self.helpers = Helpers()

    def request_forms(self):
        for index, form in enumerate(self.forms[8000:9000]):

            request_parameters = self.helpers.make_request_parameters(form.canonical_url, 4500)
            try:
                response = requests.get( request_parameters['url'],
                                          stream=True,
                                          headers=request_parameters['headers'])
                
                print index, response.status_code, request_parameters['url']
                form.status_code = response.status_code
            except:
                pass
            try:
                last_modified = response.headers['last-modified']
                print 'Last modified', last_modified
                form.last_modified = last_modified
            except:
                pass
            try:
                etag = response.headers['etag']
                print 'etag: ', etag
                if not form.current_etag:
                    form.current_etag = etag
            except:
                pass
            print
            form.save()
                
        return response


def run():
    form_request = FormRequest()
    form_request.request_forms()
