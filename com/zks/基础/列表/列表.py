# -*- coding: gbk -*-
'''
Created on 2017年5月5日

@author: Administrator
'''
list=[2,3,4,5]
list2=[7,8]
#访问列表中的值
for i in list:
    print(i)
print(list[1:3])

#更新列表
list[3]=9
print(list) 

#删除元素
del list[1]
print(list)

print(len(list))  #获得list列表的长度

print(2 in list) #元素是否存在于列表中

print(list+list2) #组合