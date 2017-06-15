#常用鼠标键盘操作

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://www.csdn.net/")
driver.find_element_by_xpath("//cite[@id='login']/a").click();

driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("zhangsan")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_class_name("logging").click()
#driver.find_element_by_class_name("logging").submit()

driver.quit()
