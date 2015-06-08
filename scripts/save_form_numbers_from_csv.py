import csv

from forms.models import Form

class FormNumber:

    def __init__(self):
        '''Replace with correct filename in root directory.'''
        self.filename = 'changed_form_report_052615.csv'

    def read_csv_to_dict(self):
        '''
        Reads values from csv file and writes the form
        numbers to the database. May need to alter 
        field names.
        '''
        with open(self.filename) as csvfile:
            form_dicts = csv.DictReader(csvfile)
            for index, row in enumerate(form_dicts):
                forms = Form.objects.filter(canonical_url=row['URL'])
                try:
                    form = forms[0]
                    '''uncomment 3 lines below for adding form
                    numbers to database
                    '''
                    # form.form_numbers = row['FORM #']
                    # print form.form_numbers, form.canonical_url
                    # print

                    '''In this section, add string that corresponds to
                    the comment in the FORM CHANGED? field for a form to
                    eliminate. Add additional strings as needed
                    '''

                    if '404' in row['FORM CHANGED?'].lower():
                        form.ignore = True
                        print form.canonical_url, '****************', row['FORM CHANGED?'], '***************'

                    form.save()
                except:
                    pass


def run():
    form_number = FormNumber()
    form_number.read_csv_to_dict()
