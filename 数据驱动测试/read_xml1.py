#读取xml文件
#获得标签信息
from xml.dom import minidom

#打开xml文档
dom=minidom.parse('info.xml')

#得到文档元素对象
root=dom.documentElement

print(root.nodeName)#节点名称
print(root.nodeValue)#节点的值，只对文本节点有效
print(root.nodeType)#节点的类型
print(root.ELEMENT_NODE)