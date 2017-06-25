#多表单切换
from selenium import webdriver
import time
import os

driver=webdriver.Chrome()
file_path='file:///'+os.path.abspath('frame.html')
driver.get(file_path)

#切换到iframe(id="if")
driver.switch_to_frame("if")

#下面可以正常的操作元素了
driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()
time.sleep(3)

driver.quit()
