#参数化搜索关键字
from selenium import webdriver

search_text=['python','selenium','text']

for text in search_text:
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.baidu.com")
    driver.find_element_by_id('kw').send_keys(text)
    driver.find_element_by_id('su').click()
    driver.quit()