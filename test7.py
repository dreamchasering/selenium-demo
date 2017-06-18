#获得验证信息
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("http://www.csdn.net/")
driver.find_element_by_xpath("//cite[@id='login']/a").click();

print('Before login==============================')

#打印当前页面title
title=driver.title
print(title)

#打印当前页面URL
now_url=driver.current_url
print(now_url)

#执行登陆
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("dreamchasering")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_class_name("logging").click()
time.sleep(5)

print('After login================================')

#再次打印当前页面title
title=driver.title
print(title)

#打印当前页面URL
now_url=driver.current_url
print(now_url)

user=driver.find_element_by_xpath("//a[@href='/dreamchasering' and @target='_blank']").text
print(user)

driver.quit()
