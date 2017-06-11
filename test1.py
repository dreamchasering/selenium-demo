#控制浏览器窗口大小、前进、后退、刷新
# coding=utf-8
from selenium import webdriver

driver=webdriver.Chrome()
#访问百度首页
first_url='http://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)

print("设置浏览器宽500，高800")
driver.set_window_size(500,800)

#访问学术页面
second_url='http://xueshu.baidu.com/'
print("now access %s" %(second_url))
driver.get(second_url)

#后退到百度首页
print("back to %s" %(first_url))
driver.back();

#前进到学术页
print("forward to %s" %(second_url))
driver.forward()

#刷新当前页面
driver.refresh()

driver.quit()