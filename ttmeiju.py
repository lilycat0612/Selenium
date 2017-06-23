#coding:utf-8
import os
import unittest
import time
from selenium import webdriver

#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys

class DownloadBtFiles(unittest.TestCase):
    def setUp(self):
        url = raw_input("Enter your website: ");
        # create a new Firefox session
        dir=os.path.dirname(__file__)
        print(dir)
        chrome_driver_path=dir+"\chromedriver.exe"
        self.driver=webdriver.Chrome(chrome_driver_path)
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get(url)


    def tearDown(self):
        self.driver.quit()
    
    def test_get_links(self):
        self.driver.execute_script("scrollTo(0,1000);") #scroll to display the file list
        

        #bt_files=self.driver.find_elements_by_css_selector("a[href*='torrent']") #download All bt files

        bt_files=self.driver.find_elements_by_css_selector("a[href*='1080p'][title*='BT']")#downlaod 'BT' files with '1080p' name

        file_count=0
        
        for file in bt_files:
          
            file.click()
            time.sleep(3)
            file_count=file_count+1
            

        #element_is_displayed=self.driver.find_element_by_css_selector("a[href*='torrent']").click()
        if file_count == len(bt_files):#make sure download all files
            print("Finish Download (%s) BT Files at:"%(file_count),time.asctime())
        else:
            print("Download (%s) BT Files at :" %(file_count),time.asctime())

if __name__=='__main__':
    unittest.main()
    
    