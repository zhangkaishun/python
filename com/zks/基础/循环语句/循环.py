# -*- coding: gbk -*-
'''
Created on 2017年5月3日

@author: Administrator
'''
temp=0
numbers=[12,14,16,17,18,33]
even=[]
odd=[]
#while循环
while len(numbers)>0:
    number=numbers.pop()
    if number%2==0:
        even.append(number)
    else:
        odd.append(number)
#for循环
for temp in even:
    print(temp)
    


    