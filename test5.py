#鼠标悬停
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

#定位到要悬停的元素
above=driver.find_element_by_xpath("//div[@id='u1']/a[8]")
#对定位到的元素执行悬停操作
ActionChains(driver).move_to_element(above).perform()

driver.quit()
