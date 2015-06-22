import pdb, pickle

from forms.models import Form


class Unignore:

    '''This class contains methods for removing
    an ignored keyword from the ignored keywords file.
    '''

    def __init__(self):
        
        self.filename = 'scripts/keywords_to_ignore.pkl'
        self.keywords = self._read_keywords_from_pickle_file()

    
    def remove_ignored_keyword(self, keyword=None):

        if keyword and keyword in self.keywords:
            self.keywords.remove(keyword)
            self._write_keywords_to_pickle_file(self.keywords)    
        
    
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
    Pass arguments to runscript to indicate keyword to be ignored:
    $ python manage.py runscript remove_ignored_keyword -v3 --script-args='manual'
    '''
    unignore = Unignore()
    keyword = None
    
    if args:
        keyword = args[0]

    else:
        print(unignore.keywords)

    unignore.remove_ignored_keyword(keyword=keyword)
