import os
from selenium import webdriver 
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

chrome = Chrome()

local_path = f'file://{os.path.dirname(os.path.realpath(__file__))}'
chrome.get(f'{local_path}/templates/click.html')
ancora = chrome.find_element(By.LINK_TEXT, 'Google')
ancora.click()