#参数化登陆
from selenium.webdriver import ActionChains

class Login():
    #登陆
    def user_login(self,driver,username,password):
        driver.find_element_by_xpath("//div[@class='header_right']/p/a[@href='/login']").click()

        driver.find_element_by_id("phone_ipt").clear()
        driver.find_element_by_id("phone_ipt").send_keys(username)
        driver.find_element_by_id("pwd_ipt").clear()
        driver.find_element_by_id("pwd_ipt").send_keys(password)
        driver.find_element_by_id("sbtn").click()

    #退出
    def user_logout(self,driver):
        above = driver.find_element_by_xpath("//div[@class='mguser']/div[@class='mguser-box']/a")
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_xpath("//ul[@class='mguser-cnt']/li[3]/a").click()
        driver.quit()
