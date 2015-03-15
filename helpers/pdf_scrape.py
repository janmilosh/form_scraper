import datetime, os, re
from urlparse import urljoin
from contextlib import closing
import pdb 

from bs4 import BeautifulSoup
import requests


class Helpers:
    def __init__(self):
        pass
        
    def request_source_page(self, url):
        return requests.get(url)

    def get_pdf_links_from_page_response(self, response):
        soup = self._make_soup(response.text)
        forms = self._return_only_pdf_links(soup)
        return forms

    def _make_soup(self, text):
        soup = BeautifulSoup(text)
        return soup

    def _return_only_pdf_links(self, soup):
        hrefs = self._find_all_links_in_soup(soup)
        return [href for href in hrefs if re.match('.*\.pdf$', href)] 

    def _find_all_links_in_soup(self, soup):
        all_links = soup.find_all('a')
        hrefs = set()
        for link in all_links:
            link = link.get('href')
            if link != None:
                hrefs.add(link)
        return hrefs

    def create_form_name(self, link):
        return link.split('/')[-1]

    def create_canonical_url(self, base_url, href):
        canonical_url = urljoin(base_url, href) 
        return canonical_url 

    def _request_document(self, base_url, doc_path, days_offset):
        request_parameters = self._make_request_parameters(base_url, doc_path, days_offset)
        
        # Stream=true only pulls headers, not full document
        with closing(requests.get( request_parameters['url'],
                                   stream=True,
                                   headers=request_parameters['headers'])
                                 ) as response:
            
            print('Getting:', request_parameters['url'])

            if response.status_code == requests.codes.not_modified:
                print('Document has not been modified since {0}, {1}'.format(
                                last_modified,response.status_code))
                
            elif response.status_code == requests.codes.ok:
                self._write_content_to_file(response,
                                        request_parameters['url'],
                                        self.pdf_directory_name)
                print('Document was modified on {0}, {1}'.format(
                                response.headers['last-modified'],
                                response.status_code))
            
            else:
                print("There was a {0} error on the response".format(response.status_code))
        return response

    def _make_request_parameters(self, base_url, doc_path, days_offset):
        url = os.path.join(base_url, doc_path)
        last_modified = self._make_time_string_with_days_offset(days_offset)            
        headers = { 'If-Modified-Since' : last_modified, }
        return { 'url': url, 'headers': headers }

    def _make_time_string_with_days_offset(self, offset_in_days):
        return (datetime.datetime.utcnow() - datetime.timedelta(days=offset_in_days)) \
                    .strftime('%a, %d %b %Y %H:%M:%S GMT')
  