'''
Created on Mar 21, 2019

@author: rallamr
'''
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


iedr = r"C:\Users\rallamr\Desktop\Ramarao\Tools\Selenium\IEDriverServer_x64_3.14.0\IEDriverServer.exe"
cap = DesiredCapabilities.INTERNETEXPLORER
cap['ignoreProtectedModeSettings']=True
cap['IntroduceInstabilityByIgnoringProtectedMode']=True

ie = webdriver.Ie(desired_capabilities=cap,executable_path=iedr)
ie.get("http://www.google.com")
ie.close()