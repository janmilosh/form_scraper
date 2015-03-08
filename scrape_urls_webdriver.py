import os, time
import cPickle as pickle

from bs4 import BeautifulSoup
import pdb
import requests
from selenium import webdriver


class Page:
    """Use webdriver to log into a website and get a list of urls.
    Page descriptions and their urls are returned in a dict.
    """

    def __init__(self, base_url, page_urls, email, password):
        self.driver = webdriver.Firefox()
        self.base_url = base_url
        self.page_urls = page_urls
        self.email = email
        self.password = password
        self.root_dir = os.getcwd()
        self.page_list = []
    
    def main(self):
        self._configure()
        self._login()
        for page_url in self.page_urls:
            urls_page = self._go_to_urls_page(page_url)
            time.sleep(10)
            self.page_list.append(urls_page)
            soup = BeautifulSoup(urls_page)
            print soup.prettify()
        self.driver.close()
        self._write_urls_page_list_to_pickle_file(self.page_list)
   
    def _configure(self):
        """Set the browser size and the amount of time we'll wait
        for things to happen.
        """
        width = 1280
        height = 800
        time_in_seconds = 10
        self.driver.set_window_size(width, height)
        self.driver.implicitly_wait(time_in_seconds)

    def _login(self):
        """Use webdriver to log in to the site from the login page."""
        self.driver.get(self.base_url + '/login.html')
        email = self.driver.find_element_by_name("email")
        email.send_keys(self.email)
        password = self.driver.find_element_by_name("pw")
        password.send_keys(self.password)
        remember = self.driver.find_element_by_name("remember")
        remember.click()
        login = self.driver.find_element_by_name("login")
        login.click()

    def _go_to_urls_page(self, page_url):
        self.driver.get(page_url)
        page = self.driver.page_source
        return page

    def _write_urls_page_list_to_pickle_file(self, page_list):
        pickle_file_path = os.path.join(self.root_dir, 'url_files', 'page_list.p', )
        pickle.dump( page_list, open( pickle_file_path, 'wb' ) )


if __name__ == '__main__':
    base_url = 'https://www.changedetection.com'
    page_urls = ('https://www.changedetection.com/monitors.html',
                 'https://www.changedetection.com/monitors.html?rclstart=100',
                 'https://www.changedetection.com/monitors.html?rclstart=200',
                 'https://www.changedetection.com/monitors.html?rclstart=300')
    email = ''
    password = ''
    pages = Page(base_url, page_urls, email, password)
    pages.main()