#捕捉客户端向服务器发送的POST请求
from selenium import webdriver
import logging

logging.basicConfig(level=logging.DEBUG)
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()
driver.quit()
