# -*- coding: gbk -*-
'''
Created on 2017��5��3��

@author: Administrator
'''
temp=0
numbers=[12,14,16,17,18,33]
even=[]
odd=[]
#whileѭ��
while len(numbers)>0:
    number=numbers.pop()
    if number%2==0:
        even.append(number)
    else:
        odd.append(number)
#forѭ��
for temp in even:
    print(temp)
    


    