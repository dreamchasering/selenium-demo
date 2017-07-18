#参数化登陆
from selenium import webdriver
from public import Login

class LoginTest():

    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.acmcoder.com/index")

    def test_login(self):
        username='name'
        password='password'

        loginService = Login()
        loginService.user_login(self.driver,username,password)
        self.driver.quit()

test=LoginTest()
test.test_login()