#coding=utf-8
__author__ = 'srv'
#!/usr/bin/python


from selenium import webdriver
from time import sleep
from tkinter import *

url='https://item.jd.com/100003687193.html' #XiaoMi NFC
#url='https://item.jd.com/100006756254.html' #Huawei


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--headless')
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(chrome_options=chromeOptions, desired_capabilities=chromeOptions.to_capabilities())
driver.get(url) 

sleep(10)
Notify=True
Cart = driver.find_element_by_id("InitCartUrl").is_enabled()

Notify = driver.find_element_by_id("btn-notify").is_displayed()

while Notify == True:
    Notify = driver.find_element_by_id("btn-notify").is_displayed()
    if Notify == False:
       break
    else:
        driver.refresh()
        sleep(60)
        
root = Tk()
text1 = Text(root)
text1.insert("insert", "XiaoMi NFC Onboard")
text1.pack()
root.mainloop()

