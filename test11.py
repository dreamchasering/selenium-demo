#sleep休眠方法
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

sleep(2)
driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()
sleep(3)

driver.quit()
