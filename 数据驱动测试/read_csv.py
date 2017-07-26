#读取csv文件
#导入csv包
import csv
#读取本地csv文件
date=csv.reader(open('info.csv','r'))

#循环输出每一行信息
'''for user in date:
    print(user)'''

#读取用户年龄
for user in date:
    print(user[1])