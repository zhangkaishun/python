# -*- coding: gbk -*-
'''
Created on 2017��5��5��
�����Ǻţ�*���ı�������������δ�����ı�������������ں�������ʱû��ָ��������������һ����Ԫ�顣����Ҳ���Բ���������δ�����ı���
@author: Administrator
'''
def pr(arg1,*other):
    print(arg1)
    for i in other:
        print(i)
pr("zks","zk","shun")
        
#��������
sum=lambda arg1,arg2:arg1+arg2
print(sum(2,3))
