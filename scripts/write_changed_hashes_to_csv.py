import csv, requests, pdb

from forms.models import Form
from helpers.pdf_scrape import Helpers

class FormWriter:
    def __init__(self):
        self.forms = Form.objects.exclude(previous_sha256='')
        self.forms = self.forms.exclude(status_code=404)
        self.forms = self.forms.exclude(status_code=400)

    def write_to_csv(self):
        print len(self.forms)
        with open('changed_forms_2015_04_29.csv', 'w') as f:
            writer = csv.writer(f)
            for index, form in enumerate(self.forms):
                if form.current_sha256 != form.previous_sha256:
                    try:
                        writer.writerow([form.source_page, form.canonical_url])
                    except:
                        print form.status_code, form.source_page, form.canonical_url


def run():
    form_writer = FormWriter()
    form_writer.write_to_csv()