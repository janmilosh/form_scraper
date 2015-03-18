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
        return [href for href in hrefs if re.match('.*\.pdf', href)] 

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

    def make_request_parameters(self, form_url, days_offset):
        last_modified = self._make_time_string_with_days_offset(days_offset)            
        headers = { 'If-Modified-Since' : last_modified, }
        return { 'url': form_url, 'headers': headers }

    def _make_time_string_with_days_offset(self, offset_in_days):
        return (datetime.datetime.utcnow() - datetime.timedelta(days=offset_in_days)) \
                    .strftime('%a, %d %b %Y %H:%M:%S GMT')
  