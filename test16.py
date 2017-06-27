#警告框处理
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
driver=webdriver.Chrome()
#driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

#鼠标悬停至“设置”链接
link=driver.find_element_by_xpath("//div[@id='u1']/a[8]")
ActionChains(driver).move_to_element(link).perform()

#打开搜索设置
driver.find_element_by_link_text("搜索设置").click()

#保存设置
element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.CLASS_NAME,"prefpanelgo")))
element.click()
time.sleep(2)

#接受警告框
driver.switch_to_alert().accept()

driver.quit()
