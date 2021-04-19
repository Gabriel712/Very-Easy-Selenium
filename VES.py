from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time


class Browser():

    def __init__(self, log = False):

        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain, application/octet-stream, application/binary, text/csv, application/csv, application/excel, text/comma-separated-values, text/xml, application/xml, application/x-msdownload, application/octet-stream, application/blob,application/vnd.ms-excel")
        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("browser.download.dir", '/')

        options = webdriver.FirefoxOptions()
        options.set_headless(False)
        driver = webdriver.Firefox(firefox_profile=fp, options = options)

        self.driver = driver

        self.log = log


    # ACESS A URL
    def Access_Url(self, url):
        self.driver.get(url)

    # GET CURRENT URL
    def Get_Url(self):
        now_url = self.driver.current_url
        return(self.driver.current_url)

    # READ XPATH
    def Read_Xpath(self, xpath):
        while True:
            try:
                self.driver.find_element_by_xpath(xpath).location_once_scrolled_into_view
                return(self.driver.find_element_by_xpath(xpath).text)
            except NoSuchElementException:
                if self.log == True:
                    print("{xpath} NOT FOUND. FUNCTION : READ XPATH".format(xpath=xpath))

    # GET URL IN A ATTRIBUTE = <a href="python.com"> = result  = 'python.com'
    def Get_Url_Xpath_Href(self, xpath):
        while True:
            try:
                return(self.driver.find_element_by_xpath(xpath).get_attribute("href"))
            except NoSuchElementException:
                if self.log == True:
                    print("{xpath} NOT FOUND. FUNCTION : GET URL XPATH HREF".format(xpath = xpath))

    # WRITE XPATH
    def Write_Xpath(self, xpath, text):
        while True:
            try:
                self.driver.find_element_by_xpath(xpath).location_once_scrolled_into_view
                self.driver.find_element_by_xpath(xpath).send_keys(text)
                break
            except NoSuchElementException:
                if self.log == True:
                    print("{xpath} NOT FOUND. FUNCTION : WRITE XPATH".format(xpath = xpath))

    # CLICK XPATH
    def Click_Xpath(self, xpath):
        while True:
            try:
                self.driver.find_element_by_xpath(xpath).location_once_scrolled_into_view
                self.driver.find_element_by_xpath(xpath).click()
                break
            except NoSuchElementException:
                if self.log == True:
                    print("{xpath} NOT FOUND. FUNCTION : CLICK XPATH".format(xpath = xpath))

    # CLEAR INPUT
    def Clear_Input(self, xpath):
        while True:
            try:
                self.driver.find_element_by_xpath(xpath).location_once_scrolled_into_view
                self.driver.find_element_by_xpath(xpath).clear()
                break
            except NoSuchElementException:
                if self.log == True:
                    print("{xpath} NOT FOUND. FUNCTION : CLEAR Input XPATH".format(xpath = xpath))

    # CLOSE BROWSER
    def Close(self):
        self.driver.quit()


    # FREE SELECT XPATH TOOL / VERY USEFUL
    def Free_Select_Xpath(self, xpath):
        while True:
            try:
                return(self.driver.find_element_by_xpath(xpath))
            except NoSuchElementException:
                if self.log == True:
                    print("{xpath} NOT FOUND. FUNCTION : FREE SELECT XPATH".format(xpath = xpath))



if __name__ == "__main__":
    my_agent_007 = Browser(log = True)
    base_url = "https://www.google.com/search?q=Python Is Amazing "
    my_agent_007.Access_Url(base_url)
