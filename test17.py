#获取当前浏览器cookie
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://www.youdao.com")

#获得cookie信息
cookie=driver.get_cookies()
#将获得cookie的信息打印
print(cookie)

driver.quit()
