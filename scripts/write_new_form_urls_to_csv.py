import csv, requests, pdb

from forms.models import Form


class FormWriter:

    '''This class contains the method for writing 
    all newly added form urls to a csv file (currently
    those without status codes.

    This could be improved upon by filtering by date
    rather than the status code.
    '''

    def __init__(self):
        self.forms = Form.objects.filter(status_code=None)

    def write_to_csv(self):
        print len(self.forms)
        with open('new_forms_2015_05_16.csv', 'w') as f:
            writer = csv.writer(f)
            for index, form in enumerate(self.forms):
                try:
                    writer.writerow([form.source_page, form.canonical_url])
                except:
                    print form.status_code, form.source_page, form.canonical_url


def run():
    form_writer = FormWriter()
    form_writer.write_to_csv()