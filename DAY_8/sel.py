
# from selenium import webdriver
# import time
# driver =webdriver.Chrome()


# print(type(driver))
# driver.get("https://pypi.org")
# time.sleep(10)



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver =webdriver.Chrome()


print(type(driver))
driver.get("https://quotes.toscrape.com/login")
time.sleep(10)
username=driver.find_element(By.XPATH,"/html/body/div/div")
username.send_keys("abcd")
time.sleep(15)
