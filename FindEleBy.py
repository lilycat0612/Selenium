#coding:utf-8
import os
import unittest
import time
from selenium import webdriver
import re

#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys

class DownloadBtFiles(unittest.TestCase):
    def setUp(self):
        # url = raw_input("Enter your website: ")
        url = 'https://www.baidu.com'
        # create a new  session
        dir=os.path.dirname(__file__)
        chrome_driver_path=dir+"\chromedriver.exe"
        self.driver=webdriver.Chrome(chrome_driver_path)
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get(url)


    def tearDown(self):
        self.driver.quit()

    def test_get_elements_by_id(self):
        print " test_get_elements_by_id"
        try:
            ids=self.driver.find_elements_by_id('u_sp')
            print"id Found"
        except Exception as e:
            print "Exception found",format(e)

        for id in ids:
            id.click()
            print "Done"
    def test_get_email_by_re(self):
        print " test_get_email_by_re"

        doc=self.driver.page_source
        emails=re.findall(r'[\w\.-]+@[\w\.-]+',doc)
       
        for email in emails:
            print(email)
        
    def test_get_hylinks_by_xpath(self):
        print " test_get_hylinks_by_xpath"
        hylinks=self.driver.find_elements_by_xpath('//*[@href]')

        for hylink in hylinks:
            print(hylink.get_attribute('href'))
        
    def test_get_hylinks_by_text(self):
        print " test_get_hylinks_by_text"
        hylinks=self.driver.find_elements_by_link_text('hao123')

        for hylink in hylinks:
            print(hylink.get_attribute('href'))     

    def test_get_hylinks_by_partial_link_text(self):
        print " find_elements_by_partial_link_text"
        hylinks=self.driver.find_elements_by_partial_link_text('123')

        for hylink in hylinks:
            print(hylink.get_attribute('href'))       
  


if __name__=='__main__':
    unittest.main()
    
    
