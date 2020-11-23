#We are going to add a class named Request that will be responsible for getting the data from the weather website.
import os
from selenium import webdriver

class Request:
    def ___init__(self, base_url):
        self._phantomjs_path= os.path.join(os.curdir, 'phantomjs/bin/phantomjs')
        self._base_url= base_url
        self.driver= webdriver.PhantomJS(self._phantomjs_path)

    def fetch_data(self, forecast,area):
        url=self._base_url.format(forecast, area=area)
        self._driver.get(url)

        if self._driver.title=='404 Not Found':
            error_message=('Could not find the area that you searching for')
            raise Exception(error_message)

        return self._driver.page_source


        """this class is very simple; the initializer defines the base URL and creates a phantomJS driver, using path wehre
        phantomjs is installed. the fetch_data method formats the url, adding the forecast option and the area."""
