# -*- coding: gbk -*-
'''
Created on 2017��5��5��
���һ�����������а���yield�ؼ��֣���ô��������Ͳ�����һ����ͨ����������һ��generator��
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