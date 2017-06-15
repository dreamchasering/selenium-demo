#鼠标右击
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("http://www.csdn.net/")
#定位到要右击的元素
right_click=driver.find_element_by_xpath("//cite[@id='login']/a")
#对定位到的元素执行点击右键的操作
ActionChains(driver).context_click(right_click).perform()

driver.quit()
