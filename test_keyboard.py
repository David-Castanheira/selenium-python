import os 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

chrome = webdriver.Chrome()

chrome.get('https://pt.wikipedia.org/wiki/Selenium_(software)')

ActionChains(chrome)\
.key_down(Keys.CONTROL)\
.send_keys("a")\
.key_up(Keys.CONTROL)\
.key_down(Keys.CONTROL)\
.send_keys("c")\
.key_up(Keys.CONTROL)\
.perform()