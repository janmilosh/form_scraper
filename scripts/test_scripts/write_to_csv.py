import csv, requests, pdb

from forms.models import Form
from helpers.pdf_scrape import Helpers

class FormWriter:
    def __init__(self):
        self.forms_with_etags = Form.objects.exclude(current_etag = '')
        self.forms_without_etags = Form.objects.filter(current_etag = '')

    def write_to_csv_files(self):
        self._write_forms_with_etags_to_csv()
        # self._write_forms_without_etags_to_csv()
    
    def _write_forms_with_etags_to_csv(self):
        with open('forms_with_etags.csv', 'wb') as f:
            writer = csv.writer(f)
            for index, form in enumerate(self.forms_with_etags):
                try:
                    writer.writerow([form.source_page, form.canonical_url])
                except:
                    print form.source_page, form.canonical_url

    def _write_forms_without_etags_to_csv(self):
        with open('forms_without_etags.csv', 'wb') as f:
            writer = csv.writer(f)
            for index, form in enumerate(self.forms_without_etags):
                try:
                    writer.writerow([form.source_page, form.canonical_url])
                except:
                    print form.source_page, form.canonical_url


def run():
    form_writer = FormWriter()
    form_writer.write_to_csv_files()