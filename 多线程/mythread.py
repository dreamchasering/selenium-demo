#自定义线程类
import threading
from time import sleep,ctime

#创建线程类
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
        self.name=name

    def run(self):
        self.func(*self.args)

def super_play(file,time):
    for i in range(2):
        print('Start playing：%s! %s' %(file,ctime()))
        sleep(time)

lists={'爱情买卖.mp3':3,'阿凡达':5,'我和你':4}

threads=[]

for file,time in lists.items():
    t=MyThread(super_play,(file,time),super_play.__name__)
    threads.append(t)

if __name__=='__main__':
    #启动线程
    for i in range(len(lists)):
        threads[i].start()
    for i in range(len(lists)):
        threads[i].join()
    print('end:%s' %ctime())