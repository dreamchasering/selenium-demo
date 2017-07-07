#处理HTML5的视频播放
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("http://videojs.com/")

video=driver.find_element_by_xpath("html/body/section[1]/div/video")

#返回播放文件地址
url=driver.execute_script("return arguments[0].currentSrc;",video)
print(url)

#播放视频
print("start")
driver.execute_script("return arguments[0].play()",video)

#播放15秒钟
sleep(15)

#暂停视频
print("sleep")
driver.execute_script("arguments[0].pause()",video)

driver.quit()
