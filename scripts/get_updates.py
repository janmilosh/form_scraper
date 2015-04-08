import requests, pdb

from forms.models import Form
from helpers.pdf_scrape import Helpers


class Updates:
    def __init__(self):
        self.forms = Form.objects.all()
        self.helpers = Helpers()

    def get_updates(self):
        for index, form in enumerate(self.forms):

            request_parameters = self.helpers.make_request_parameters(form.canonical_url, 30)
            try:
                response = requests.get( request_parameters['url'],
                                          stream=True,
                                          headers=request_parameters['headers'])
                
                if response.status_code == requests.codes.ok:
                    print index, form.canonical_url
                    print 'Document was modified on {0}, {1}'.format(
                                  response.headers['last-modified'],
                                  response.status_code)
                    print

            except:
                pass
            
        return response


def run():
    updates = Updates()
    updates.get_updates()
