# -*- coding: gbk -*-
'''
Created on 2017��5��5��
1��������ͬһ�����������Ρ�����ʱ���ͬһ��������ֵ���Σ���һ��ֵ�ᱻ��ס
2 �������벻�ɱ䣬���Կ��������֣��ַ�����Ԫ��䵱�������б�Ͳ���
@author: Administrator
'''
from email.policy import strict
from platform import dist


map={"zks":1,"kai":2,"shun":3}
#��������
print(map["zks"])
#�޸�����
map["zks"]=8
print(map["zks"])

#ɾ���ֵ�����
del map["zks"]  #ɾ����"zks"
map.clear()   #����ֵ�
del map    #����ֵ�
map={"zks":1,"kai":2,"shun":3}

