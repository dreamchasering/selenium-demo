#通过tag name的定位方式定位一组元素
from selenium import webdriver
import os,time

driver=webdriver.Chrome()
file_path='file:///'+os.path.abspath('checkbox.html')
driver.get(file_path)

#选择页面上所有的tag name为input的元素
inputs=driver.find_elements_by_tag_name('input')

#然后从中过滤出type为checkbox的元素，单击勾选
for i in inputs:
    if i.get_attribute('type')=='checkbox':
        i.click()
        time.sleep(1)

driver.quit()