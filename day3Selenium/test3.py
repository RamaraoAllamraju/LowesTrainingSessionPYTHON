'''
Created on Mar 20, 2019

@author: rallamr
'''


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

cdm = ChromeDriverManager()
driver = webdriver.Chrome(cdm.install())
driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
sel = Select(driver.find_element_by_id("select-demo"))
sel.select_by_value("Monday")
time.sleep(5)
sel.select_by_index(4)
time.sleep(5)
sel.select_by_visible_text("Tuesday")

sel.deselect_by_visible_text("Tuesday")