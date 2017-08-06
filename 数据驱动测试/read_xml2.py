#读取xml文件
#获得任意标签名
from xml.dom import minidom

#打开xml文档
dom=minidom.parse('info.xml')

#得到文档元素对象
root=dom.documentElement

tagname=root.getElementsByTagName('browser')#可以通过标签名获取标签，所获取的对象以数组形式存放
print(tagname[0].tagName)

tagname=root.getElementsByTagName('login')
print(tagname[1].tagName)

tagname=root.getElementsByTagName('province')
print(tagname[2].tagName)