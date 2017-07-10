#线性测试实例
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.acmcoder.com/index")

#登陆
driver.find_element_by_xpath("//div[@class='header_right']/p/a[@href='/login']").click()

driver.find_element_by_id("phone_ipt").clear()
driver.find_element_by_id("phone_ipt").send_keys("15927265653")
driver.find_element_by_id("pwd_ipt").clear()
driver.find_element_by_id("pwd_ipt").send_keys("liuheng0824")
driver.find_element_by_id("sbtn").click()

#退出
above=driver.find_element_by_xpath("//div[@class='mguser']/div[@class='mguser-box']/a")
ActionChains(driver).move_to_element(above).perform()
driver.find_element_by_xpath("//ul[@class='mguser-cnt']/li[3]/a").click()
driver.quit()