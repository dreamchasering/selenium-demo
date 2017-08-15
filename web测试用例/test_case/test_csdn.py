from selenium import webdriver
import unittest
import time


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.csdn.net"


    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//cite[@id='login']/a").click();
        time.sleep(2)
        title = driver.title
        #print(title)
        self.assertEquals(title, "帐号登录")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()