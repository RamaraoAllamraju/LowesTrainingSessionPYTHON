'''
Created on Mar 21, 2019

@author: rallamr
'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

import time

def first():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.amazon.in/")
    driver.maximize_window()

    time.sleep(5)

    mover = driver.find_element_by_xpath("//*[text()='Your Orders' and @class='nav-line-2']")
    ac = ActionChains(driver)
    ac.move_to_element(mover).pause(5)
    signin = driver.find_element_by_xpath("//*[text()='Sign in' and @class='nav-action-inner']")
    ac.click(signin).pause(5)

    ac.perform()
    driver.close()


def second():
    #Not working
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.amazon.in/")

    ele = driver.find_element_by_xpath("//*[@class='nav-line-2' and text()='Category']")
    ac = ActionChains(driver)
    #ac.move_to_element(ele).pause(5)
    ac.click(ele).pause(5)
    ele = driver.find_element_by_xpath("//*[text()='Amazon Prime Video'][0]")
    ac.move_to_element(ele).pause(5)
    ele = driver.find_element_by_xpath("//*[text()='Movies' and @class='nav-text']")
    ac.click(ele).pause(5)
    
    ac.perform()
    
    validatethebutton = driver.find_element_by_xpath("//*[@alt='Join Prime']").is_displayed()
    if(validatethebutton):
        print("Successfully clicked")

    driver.close()


def third():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.amazon.in/")
    driver.maximize_window()

    time.sleep(5)

    mover = driver.find_element_by_xpath("//*[text()='Your Orders' and @class='nav-line-2']")
    ac = ActionChains(driver)
    ac.move_to_element(mover).pause(5)
    signin = driver.find_element_by_xpath("//*[text()='Your Wish List']")
    ac.move_to_element(signin).pause(5)
    ac.click(signin)
    ac.perform()
    print(driver.find_element_by_xpath("//input[@id='continue']").is_displayed())
    driver.close()


def draganddropteset():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://jqueryui.com/droppable/")
    
    time.sleep(5)
    
    driver.switch_to_frame(0)
    ac = ActionChains(driver)
     
    drag = driver.find_element_by_id("draggable")
    drop = driver.find_element_by_id("droppable")

    ac.drag_and_drop(drag, drop).perform()
    time.sleep(5)
    driver.close()



draganddropteset()


