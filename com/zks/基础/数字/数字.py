# -*- coding: gbk -*-
'''
Created on 2017��5��5��

@author: Administrator
'''
#��������ת��
from random import choice, randrange, random, shuffle

list=[2,3,4,5]
a=10
print(a)
b=float(10) # ǿ��ת��Ϊ������
print(b)
# ���ֺ���
print(max(2,3,4))  #ȡ���ֵ
print(pow(2,3))    #����

#�������       
print(choice(range(10)))  # range ����һ�������ڵ���  choice���ѡ��һ�� 
print("----")
print(randrange(2,10,2)) #��������ָ���������������е�һ�������������ȱʡֵΪ1��
print(random())       #�������0��1֮�����
shuffle(list) #������Ԫ���������
print(list)

print