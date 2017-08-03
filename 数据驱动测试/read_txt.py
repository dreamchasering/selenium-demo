#读取txt文件
user_file=open('user_info.txt','r')
lines=user_file.readlines()
user_file.close()

for line in lines:
    username=line.split(',')[0]
    password=line.split(',')[1]
    print(username,password)