# -*- coding: gbk -*-
'''
Created on 2017年5月5日

@author: Administrator
'''
#数字类型转化
from random import choice, randrange, random, shuffle

list=[2,3,4,5]
a=10
print(a)
b=float(10) # 强制转化为浮点型
print(b)
# 数字函数
print(max(2,3,4))  #取最大值
print(pow(2,3))    #求幂

#随机函数       
print(choice(range(10)))  # range 产生一个返回内的数  choice随机选择一个 
print("----")
print(randrange(2,10,2)) #方法返回指定递增基数集合中的一个随机数，基数缺省值为1。
print(random())       #随机生成0到1之间的数
shuffle(list) #将序列元素随机排序
print(list)

print