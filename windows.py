#coding:utf-8
import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class DownloadBtFiles(unittest.TestCase):
    def setUp(self):
        # url ='https://'+raw_input("Enter your website without https://: ")
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

  
        
    def test_back_forword_and_get_url(self):
        try:
            hylink=self.driver.find_element_by_link_text('hao123')
        except Exception as e:
            print "Exception found",format(e)
        
        hylink.click()

        print self.driver.current_url

        time.sleep(5)
        self.driver.back()
        print 'Move back to:'+self.driver.current_url
        time.sleep(5)
        self.driver.forward()
        print 'Move forword to:'+self.driver.current_url
        time.sleep(5)
        # if str(self.driver.title).contains('hao123'):
        #     print "DONE"

    def test_scroll(self):

        ele=self.driver.find_element_by_tag_name('html')
        time.sleep(5)
        ele.send_keys(Keys.END)
        time.sleep(5)
        ele.send_keys(Keys.HOME)
        time.sleep(5)

    def test_get_browser_version(self):
        print(self.driver.capabilities['version'])

    def test_open_new_tab(self):
        try:
           self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
           print "New Tab"
        except Exception as e:
            print "Exception found",format(e)
        self.driver.get('www.bing.com')
        time.sleep(30)
        print self.driver.current_url

    def test_set_size(self):
        self.driver.set_window_size(524,768)
        time.sleep(3)
        print self.driver.get_window_size()
        self.driver.maximize_window()
        time.sleep(3)



if __name__=='__main__':
    unittest.main()
    # verbosity=2
    
    
