# -*- coding: gbk -*-
'''
Created on 2017��5��5��

@author: Administrator
'''
list=[2,3,4,5]
list2=[7,8]
#�����б��е�ֵ
for i in list:
    print(i)
print(list[1:3])

#�����б�
list[3]=9
print(list) 

#ɾ��Ԫ��
del list[1]
print(list)

print(len(list))  #���list�б�ĳ���

print(2 in list) #Ԫ���Ƿ�������б���

print(list+list2) #���