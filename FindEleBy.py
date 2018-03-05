#coding:utf-8
import os
import unittest
import time
from selenium import webdriver
import re
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

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
        doc=self.driver.page_source
        emails=re.findall(r'[\w\.-]+@[\w\.-]+',doc)
       
        for email in emails:
            print(email)
        
    def test_get_hylinks_by_xpath(self):
        hylinks=self.driver.find_elements_by_xpath('//*[@href]')

        for hylink in hylinks:
            print(hylink.get_attribute('href'))
        
    def test_get_hylinks_by_text(self):
        hylinks=self.driver.find_elements_by_link_text('hao123')

        for hylink in hylinks:
            print(hylink.get_attribute('href'))     

    def test_get_hylinks_by_partial_link_text(self):
        hylinks=self.driver.find_elements_by_partial_link_text('123')

        for hylink in hylinks:
            print(hylink.get_attribute('href'))       

    def test_click_radio_button(self):
        self.driver.get('https://www.zkoss.org/zkdemo/input/radio_button')

        self.driver.implicitly_wait(30)
        try:
            eles=self.driver.find_elements_by_xpath("//*[@type='radio']")
            eles=self.driver.find_elements_by_xpath('//*[@type="radio"]')

        except Exception as e:
            print "Exception found",format(e)

        for ele in eles:
            ele.click()
        time.sleep(5)
    
    def test_click_check_box(self):
        self.driver.get('http://demos.dojotoolkit.org/dijit/tests/form/test_CheckBox.html')

        self.driver.implicitly_wait(300)
        try:
            ele=self.driver.find_element_by_xpath(".//*[contains(text(),'cb7')]")
        except Exception as e:
            print "Exception found",format(e)

        ele.click()
        time.sleep(5)

    def test_get_class_name(self): 
        try:
            eles=self.driver.find_elements_by_xpath(".//*[@name]")
        except Exception as e:
            print "Exception found",format(e)
       
        for ele in eles:
            print ele.get_attribute('name')
    

    def test_get_img(self): 
        try:
            eles=self.driver.find_elements_by_tag_name("img")
        except Exception as e:
            print "Exception found",format(e)
       
        for ele in eles:
            print ele.text
            print ele.location
            print ele.tag_name
            #print ele.size

    def test_right_click(self):
        
        try:
            ele=self.driver.find_element_by_link_text('hao123')
            print 'Find hao123'
        except Exception as e:
            print "Exception found",format(e)

        action=ActionChains(self.driver)
        
        action.context_click(ele).perform()

        time.sleep(10)

    def test_mouse_hover(self):
        
        try:
            ele=self.driver.find_element_by_link_text('hao123')

        except Exception as e:
            print "Exception found",format(e)

        action=ActionChains(self.driver).move_to_element(ele)
        action.perform()

        time.sleep(10)
    def test_exec_JS(self):
        
        try:
            self.driver.execute_script("document.body.style_zoom='150%';")
            self.driver.execute_script("window.alert('hao123');")

        except Exception as e:
            print "Exception found",format(e)
        time.sleep(10)
        alert=self.driver.switch_to_alert()
        alert.accept()


    def test_1select_all_text(self):
        
        try:
            ele=self.driver.find_element_by_css_selector('body')
        except Exception as e:
            print "Exception found",format(e)

        time.sleep(10)
        ele.send_keys(Keys.CONTROL+'a')

if __name__=='__main__':
    unittest.main()
    # verbosity=2
    
    
