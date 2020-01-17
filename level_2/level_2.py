from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from fake_useragent import UserAgent

useragent = UserAgent()
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", useragent.random)
driver = webdriver.Firefox(executable_path='/home/cristian/Downloads/geckodriver-v0.26.0-linux64/geckodriver')

url = "http://158.69.76.135/level2.php"
driver.get(url)
"""
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36 """
for i in range(5):

    val = driver.find_element_by_name('id')
    buttom = driver.find_element_by_name('holdthedoor')
    val.send_keys('12')
    buttom.click()

driver.close()
