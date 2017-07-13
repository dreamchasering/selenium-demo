from selenium import webdriver
from public import Login

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.acmcoder.com/index")

loginService = Login()
#调用登陆模块
loginService.user_login(driver)
#调用退出模块
loginService.user_logout(driver)
