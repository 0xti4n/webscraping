from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(executable_path='/home/cristian/Downloads/geckodriver-v0.26.0-linux64/geckodriver')

url = "http://158.69.76.135/level0.php"
driver.get(url)


for i in range(5):
    val = driver.find_element_by_name('id')
    buttom = driver.find_element_by_name('holdthedoor')
    val.send_keys('12')
    buttom.click()

driver.close()