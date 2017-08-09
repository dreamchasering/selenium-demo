#读取xml文件
#获得标签对之间的数据
from xml.dom import minidom

#打开xml文档
dom=minidom.parse('info.xml')

#得到文档元素对象
root=dom.documentElement

provinces=root.getElementsByTagName('province')
cities=root.getElementsByTagName('city')

#获得第二个province标签对的值
p2=provinces[1].firstChild.data#firstChild属性返回被选节点的第一个子节点；data表示获取该节点的数据
print(p2)

#获得第一个city标签对的值
c1=cities[0].firstChild.data
print(c1)

#获得第二个city标签对的值
c2=cities[1].firstChild.data
print(c2)