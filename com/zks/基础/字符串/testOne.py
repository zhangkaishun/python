# -*- coding: gbk -*-
'''
Created on 2017��5��3��

@author: Administrator
'''
from builtins import str
str="hello world"
print(str[0])  #��ȡ�ַ���ĳ��λ���ϵ��Ը�
print(str[1:3])  #��ȡ�ַ���ĳ��������ַ���������ָ������������Ǹ�
print(str[:3]+"kk") #:3 ����ȡ�ַ�������Ϊ0 ��2 ���ַ�
strTwo=str.replace("world","zks")
print(strTwo)
print(r"\n") #�����е��ַ�������ֱ�Ӱ����������˼��ʹ�ã�û��ת��������ܴ�ӡ���ַ�
print(str*2) # * �����ظ����

errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print(errHTML)
