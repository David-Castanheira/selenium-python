from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configuração do Selenium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessando a URL definida
driver.get('https://www.google.com')
