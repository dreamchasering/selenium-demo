#通过XPath或CSS查找一组元素
from selenium import webdriver
import os,time

driver=webdriver.Chrome()
file_path='file:///'+os.path.abspath('checkbox.html')
driver.get(file_path)

#通过XPath找到type=checkbox的元素
#checkboxes=driver.find_elements_by_xpath("//input[@type='checkbox']")

#通过CSS的方式找到type=checkbox的元素
checkboxes=driver.find_elements_by_css_selector('input[type=checkbox]')

for checkbox in checkboxes:
    checkbox.click()
    time.sleep(1)

#打印当前页面上type为checkbox的个数
print(len(checkboxes))

#把页面上最后1个checkbox的钩去掉
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
time.sleep(1)

driver.quit()