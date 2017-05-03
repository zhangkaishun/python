# -*- coding: gbk -*-
'''
Created on 2017年5月3日

@author: Administrator
'''
from builtins import str
str="hello world"
print(str[0])  #获取字符串某个位置上的自负
print(str[1:3])  #获取字符串某个区间的字符，不包括指定索引的最后那个
print(str[:3]+"kk") #:3 代表取字符串索引为0 到2 的字符
strTwo=str.replace("world","zks")
print(strTwo)
print(r"\n") #：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符
print(str*2) # * 代表重复输出

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
