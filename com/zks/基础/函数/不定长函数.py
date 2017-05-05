# -*- coding: gbk -*-
'''
Created on 2017年5月5日
加了星号（*）的变量名会存放所有未命名的变量参数。如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量
@author: Administrator
'''
def pr(arg1,*other):
    print(arg1)
    for i in other:
        print(i)
pr("zks","zk","shun")
        
#匿名函数
sum=lambda arg1,arg2:arg1+arg2
print(sum(2,3))
