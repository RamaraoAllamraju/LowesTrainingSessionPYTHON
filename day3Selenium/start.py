'''
Created on Mar 20, 2019

@author: rallamr
'''
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time

driver = ""

def chrome1():
    CHROMEDRIVER = "C:\\Users\\rallamr\\Desktop\\Ramarao\\Tools\\Selenium\\chromedriver_win32\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
    driver.get("http://demo.guru99.com/v1/index.php")
    driver.maximize_window()
    
    str = driver.find_element_by_xpath("//*[@class='barone']")
    print(str)
    driver.find_element_by_name("uid").send_keys("mngr185588")
    driver.find_element_by_name("password").send_keys("eqadabY")
    driver.find_element_by_name("btnLogin").click()
    time.sleep(5)   
    driver.close()


# # Another way to do it
def chrome2():
    wb = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    wb.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
    sel = Select(wb.find_element_by_id("select-demo"))
    sel.select_by_value("Monday")
    
    #wb.close()


def IR():
    iedr = r"C:\Users\rallamr\Desktop\Ramarao\Tools\Selenium\IEDriverServer_x64_3.14.0\IEDriverServer.exe"
    ie = webdriver.Ie(executable_path=iedr)
    ie.get("http://www.google.com")
    ie.close()

def openDriver(url):
    wb = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    wb.get("http://www.gmail.com")


chrome2()
