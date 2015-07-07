import pdb, pickle

from forms.models import Form


class Ignorer:

    '''This class contains the method for finding
    forms to ignore based on a keyword in the
    canonical url.
    '''

    def __init__(self):
        self.forms = Form.objects.exclude(ignore=True)
        self.filename = 'scripts/keywords_to_ignore.pkl'

        self.keywords = self._read_keywords_from_pickle_file()

    
    def ignore_forms_with_keywords(self, new_keyword=None, save=False):
        count = 0

        if new_keyword and new_keyword not in self.keywords:
            self.keywords.append(new_keyword)

        if save:
            self._write_keywords_to_pickle_file(self.keywords)    
        
        for form in self.forms:
            for word in self.keywords:
                if word.lower() in form.canonical_url.lower():
                    count += 1
                    print(count, word, form.canonical_url)
                    if save:
                        form.ignore = True
                        form.save()
                        print('This form was ignored.')

    def ignore_404s(self):
        count = 0
        status_codes = (500, 404)
        # add 403's to these status codes once new, fixed versions of
        # the urls have been added to the database.
        for form in self.forms:
            for status_code in status_codes:
                if form.status_code == status_code:
                    count += 1
                    form.ignore = True
                    form.save()
                    print(count, form.status_code, form.canonical_url)

    
    def _write_keywords_to_pickle_file(self, keywords):
        pkl_file = open(self.filename, 'wb')
        pickle.dump(keywords, pkl_file)
        pkl_file.close()

    def _read_keywords_from_pickle_file(self):
        pkl_file = open(self.filename, 'rb')
        keywords = pickle.load(pkl_file)
        pkl_file.close()
        return keywords

                    
def run(*args):
    '''
    Pass arguments to runscript to indicate keyword as a string and if save add an save as first arg,
    otherwise add check as first argument:
    $ python manage.py runscript ignore_forms_by_keyword_or_status_code -v3 --script-args=check 'formulary change update'
    $ python manage.py runscript ignore_forms_by_keyword_or_status_code -v3 --script-args=save 'formulary change update'
    $ python manage.py runscript ignore_forms_by_keyword_or_status_code -v3 --script-args=check
    $ python manage.py runscript ignore_forms_by_keyword_or_status_code -v3 --script-args=save
    '''
    ignorer = Ignorer()
    new_keyword = None
    save = False
    
    if args:
        if len(args) == 2:
            new_keyword = args[1]
        
        if args[0] == 'save':
            save = True


    ignorer.ignore_forms_with_keywords(new_keyword=new_keyword, save=save)
    # ignorer.ignore_404s()
    