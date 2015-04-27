import requests, pdb, csv, pprint

from forms.models import Form
from helpers.pdf_scrape import Helpers


class Etags:
    def __init__(self):
        self.forms_with_etags = Form.objects.exclude(current_etag = '')

    def compare_etags(self):
        forms = []
        for index, form in enumerate(self.forms_with_etags[9000:]):
            
            try:
                response = requests.get( form.canonical_url, stream=True, )
            except:
                pass

            try:
                print index, 'content-length:', response.headers['content-length']
                new_etag = response.headers['etag']
                if form.current_etag not in new_etag:
                    print "old etag", form.current_etag
                    print "new etag", new_etag
                    forms.append([form.source_page, form.canonical_url])
            except:
                pass

        pprint.pprint(forms)
        print "There were " + str(len(forms)) + "forms."
        self.write_to_csv(forms)

    def write_to_csv(self, form_list):
        with open('forms_with_changed_etags.csv', 'a') as f:
            writer = csv.writer(f)
            
            try:
                writer.writerows(form_list)
            except:
                print '**************************************************************************'
                print "Could not write to CSV!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                print '**************************************************************************'


def run():
    etags = Etags()
    etags.compare_etags()