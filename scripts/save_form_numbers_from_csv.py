import csv

from forms.models import Form

class FormNumber:

    def __init__(self):
        '''Replace with correct filename in root directory.'''
        self.filename = 'changed_form_report_061015.csv'

    def read_csv_to_dict(self):
        '''
        Reads values from csv file and writes the form
        numbers to the database. May need to alter 
        field names.
        '''
        with open(self.filename) as csvfile:
            form_dicts = csv.DictReader(csvfile)
            for index, row in enumerate(form_dicts):
                print(index,)
                forms = Form.objects.filter(canonical_url=row['URL'])
                
                form = forms[0]
                '''uncomment 4 lines below for adding form
                numbers to database
                '''
                if row['NUMBER'] != 'NEW':
                    form.form_numbers = row['NUMBER']
                    print(form.form_numbers, form.canonical_url)
                    print

                '''In this section, add string that corresponds to
                the comment in the NOTES field for a form to
                eliminate. Add additional strings as needed
                '''
                ignore_comments = (
                    'Not a PA',
                    'ERROR',
                    'ignore',
                    'Redirected',
                    )
                for comment in ignore_comments:

                    if comment in row['NOTES']:
                        form.ignore = True
                        print(form.canonical_url, '****************', row['NOTES'], '***************')


                # if '404' in row['FORM CHANGED?'].lower():
                #     form.ignore = True
                #     print(form.canonical_url, '****************', row['FORM CHANGED?'], '***************')

                form.save()
                

def run():
    form_number = FormNumber()
    form_number.read_csv_to_dict()
