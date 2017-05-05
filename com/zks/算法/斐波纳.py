# -*- coding: gbk -*-
'''
Created on 2017年5月5日

@author: Administrator
'''
a,b=0,1
while b<10: 
    print(b)
    a,b=b,a+b  #右边的表达式会在赋值变动之前执行。右边表达式的执行顺序是从左往右的。