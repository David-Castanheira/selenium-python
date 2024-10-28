import os
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome = Chrome()

local_path = f'file://{os.path.dirname(os.path.realpath(__file__))}/'
chrome.get(f'{local_path}/templates/exemplo-05.html')

languages = chrome.find_elements(By.NAME, 'language')
for language in languages:
    if language.get_attribute('value') == 'Python':
        language.click()
        time.sleep(1.0)
for language in languages:
    if language.is_selected():
        print(language.get_attribute('value'))
        time.sleep(1.0)