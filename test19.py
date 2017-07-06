#调用JavaScript控制滚动条
'''WebDriver提供了execute_script（）方法来执行JavaScript代码
用于调整浏览器滚动条位置的JavaScript代码如下：
window.scrollTo(左边距,上边距)'''
from selenium import webdriver
from time import sleep

#访问百度
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

#搜索
driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()
sleep(2)

#设置浏览器窗口大小
driver.set_window_size(600,600)

#通过javascript设置浏览器窗口的滚动条位置
js="window.scrollTo(100,450);"
driver.execute_script(js)
sleep(3)

driver.quit()