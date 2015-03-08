import os, time
import cPickle as pickle

import pprint

from bs4 import BeautifulSoup
import pdb

class Parse:
    def __init__(self):
        self.root_dir = os.getcwd()
        
    def main(self):
        pickle_path = os.path.join(self.root_dir, 'url_files', 'url_list.p')
        pages_list = pickle.load( open(pickle_path, 'rb') )
        self._create_url_dict(pages_list)

    def _create_url_dict(selfl, pages_list):
        links = []
        labels = []

        for urls_page in pages_list:
            soup = BeautifulSoup(urls_page)
            
            soup = soup.body.extract()
            soup.form.decompose()
            soup.p.decompose()
            soup.script.decompose()
            unwanted = soup.select('.bbord')
            
            for elem in unwanted:
                elem.decompose()

            raw_link_list = soup.select('a[rel="nofollow"]')
            
            for elem in raw_link_list:
                href = elem['href']
                elem.decompose()
                links.append(href)

            raw_label_list = soup.select('.lbord.ctd a')
            for elem in raw_label_list:
                title = elem['title']
                if title:
                    labels.append(title)
        
        url_dict = dict(zip(labels, links))
        pprint.pprint(url_dict)


if __name__ == '__main__':
    parse = Parse()
    parse.main()            