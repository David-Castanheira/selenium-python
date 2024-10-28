import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(0.5)
driver.get("https://www.facebook.com")

bt_create_new_acc = driver.find_element(By.XPATH, "//a[text()='Criar nova conta']")
bt_create_new_acc.click()

first_name = driver.find_element(By.NAME, "firstname")
first_name.send_keys('Marco Tulio')
last_name = driver.find_element(By.NAME, "lastname")
last_name.send_keys('Jeunon')

email = driver.find_element(By.NAME, "reg_email__")
email.send_keys('marcotuliojeunon@faculdadeimpacta.com.br')
passwd = driver.find_element(By.NAME, "reg_passwd__")
passwd.send_keys('1234')

month = driver.find_element(By.ID, "month")
sel = Select(month)
sel.select_by_index(11)

day = driver.find_element(By.ID, "day")
sel = Select(day)
sel.select_by_index(11)

year = driver.find_element(By.ID, "year")
sel = Select(year)
sel.select_by_value('1995')

sex_male = driver.find_element(By.XPATH, "//label[text()='Masculino']")
sex_male.click()
botao_signUp = driver.find_element(By.XPATH, "//button[text()='Cadastre-se']")
botao_signUp.click()
time.sleep(40)

error_msg = driver.find_element()