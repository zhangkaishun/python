# -*- coding: gbk -*-
'''
Created on 2017��5��5��

@author: Administrator
'''
import sys


list=["zks","ksi","shun"]
it=iter(list)
for x in it:    
    print(x)
    
print("----------------")
list=["zks","ksi","shun"]
it=iter(list)
while(True):
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
