import os 
from selenium import webdriver 
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

local_path = f'file://{os.path.dirname(os.path.realpath(__file__))}/'

chrome.get(f'{local_path}/templates/youtube.html')
botao = chrome.find_element(By.TAG_NAME, 'button')
webdriver.ActionChains(chrome).context_click(botao).perform()