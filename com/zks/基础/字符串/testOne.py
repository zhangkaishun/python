# -*- coding: gbk -*-
'''
Created on 2017��5��3��

@author: Administrator
'''
from builtins import str
str="hello world"
print(str[0])  #��ȡ�ַ���ĳ��λ���ϵ��ַ�
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
print("------------")
print("abcdef".center(10))  #����һ��ָ���Ŀ�� width ���е��ַ�����fillchar Ϊ�����ַ���Ĭ��Ϊ�ո�
print("abcdfsab".count("ab"))
print("abcdef".find("bk")) #�������ַ��������� ��������ڣ�����-1
print("abcdef".isalpha()) #������һ����ĸ
print("------2")
list=["3","4","5","6"]
print("_".join(list)) #�������е�Ԫ����ָ���ַ��������µ��ַ���

str2="abcedf"
print(str2.replace("bc", "kkk")) #�滻�ַ���
str3="fsf,dksfjsl,fsldf"
print(str3.split(sep=","))#ͨ��ָ���ָ������ַ���������Ƭ���������num ��ָ��ֵ������ָ� num �����ַ���
str3="fsf\rDksfjsl\rfsldf"
print(str3.splitlines()) #������('\r', '\r\n', \n')�ָ�������һ������������ΪԪ�ص��б�������� keepends Ϊ False�����������з������Ϊ True���������з�
print(str3.swapcase())  #���ַ�����дת��ΪСд��Сдת��Ϊ��д
