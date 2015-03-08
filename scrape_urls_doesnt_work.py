import os, re
import pdb
from bs4 import BeautifulSoup

import requests


class Page:
    """Use requests to log into a website and get a list of urls.
    Urls are returned in a list.
    """

    def __init__(self, base_url, page_url, email, password):
        self.base_url = base_url
        login_path = 'login.html'
        self.login_url = os.path.join(base_url, login_path)
        self.page_url = page_url
        self.email = email
        self.password = password

    def get_urls(self):
        """The main method that calls the other methods
        and saves links to the database.
        """

        with requests.Session() as session:
            self._login_to_site(session)                                
            # page = self._get_page_containing_links(session)
        
    def _login_to_site(self, session):
        """Use the requests session to login to the site."""
        session.get(self.login_url)
        login_data = dict(email=self.email,
                          pw=self.password,
                          frompage=self.login_url,
                          login='log in')
        page = session.post(self.login_url, data=login_data, headers={'Referer': self.base_url})
        page = session.get(self.base_url)
        pdb.set_trace()
        soup = BeautifulSoup(page.text)
        print(soup.prettify())

    def _get_page_containing_links(self):
        pass


if __name__ == '__main__':
    base_url = 'https://www.changedetection.com/'
    email = ''
    password = ''
    urls = Page(base_url, '', email, password)
    urls.get_urls()