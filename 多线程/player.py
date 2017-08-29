#优化线程的创建
from time import sleep,ctime
import threading

#创建超级播放器
def super_player(file,time):
    for i in range(2):
        print('Start playing: %s! %s' %(file,ctime()))
        sleep(time)

#播放的文件与文件时长
lists={'爱情买卖.mp3':3,'阿凡达.mp4':5,'我和你':4}

threads=[]

#创建线程
for file,time in lists.items():
    t=threading.Thread(target=super_player,args=(file,time))
    threads.append(t)

if __name__=='__main__':
    #启动线程
    for t in range(len(lists)):
        threads[t].start()
    for t in range(len(lists)):
        threads[t].join()

    print('end: %s' %ctime())