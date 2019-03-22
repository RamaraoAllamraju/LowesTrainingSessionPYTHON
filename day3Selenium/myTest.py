from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.saucedemo.com/")
driver.find_element_by_id("user-name").send_keys("standard_user")
driver.find_element_by_id("password").send_keys("secret_sauce")
#driver.find_element_by_("btn_action").click()
driver.find_element_by_class_name("btn_action").click()
time.sleep(5)
#driver.find_element_by_xpath("//div[@class='inventory_list']//div[1]//div[3]//button[1]").click()
print("Here")

mywblist = driver.find_elements_by_xpath("//*[@class='btn_primary btn_inventory']")
print("Length :",len(mywblist))
#driver.close()
print("End")
