'''
Created on Mar 21, 2019

@author: rallamr
'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pip._vendor.urllib3.util.timeout import current_time
import datetime


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.in/")
print(datetime.datetime.now())
driver.implicitly_wait(100)
#driver.maximize_window()
print(datetime.datetime.now())
print(19)
wdw = WebDriverWait(driver,20)
mover = wdw.until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[text()='Account & Lists' and @class='nav-line-2']")))
#driver.find_element_by_xpath("//*[text()='Your Orders' and @class='nav-line-2']")
print(23)
ac = ActionChains(driver)
ac.move_to_element(mover)

signin = wdw.until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[text()='Sign in' and @class='nav-action-inner']")))
print(28)
#signin = driver.find_element_by_xpath("//*[text()='Sign in' and @class='nav-action-inner']")
ac.perform()
driver.close()
print(32)