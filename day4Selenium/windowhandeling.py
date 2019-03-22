# TOOLSQA
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.toolsqa.com/automation-practice-switch-windows/")
time.sleep(5)
driver.find_element_by_id("button1").click()
print(driver.window_handles)
print(driver.title)

parent = driver.current_window_handle
time.sleep(5)
#driver.switch_to_window("QA Automation Tools Tutorial")
driver.switch_to_window(driver.window_handles[1])
time.sleep(5)
print(driver.title)

driver.switch_to_window(parent)
print(driver.title)

#COMMENT




