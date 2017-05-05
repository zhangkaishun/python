# -*- coding: gbk -*-
'''
Created on 2017年5月5日
如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
@author: Administrator
'''
def fbnq():
    a,b=0,1
    while b<10:
        yield b
        a,b=b,a+b
        
fbnqre=fbnq()
for i in fbnqre:
    print(i)