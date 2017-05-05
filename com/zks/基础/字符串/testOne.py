# -*- coding: gbk -*-
'''
Created on 2017年5月3日

@author: Administrator
'''
from builtins import str
str="hello world"
print(str[0])  #获取字符串某个位置上的字符
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
print("------------")
print("abcdef".center(10))  #返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
print("abcdfsab".count("ab"))
print("abcdef".find("bk")) #返回在字符串中索引 如果不存在，返回-1
print("abcdef".isalpha()) #至少有一个字母
print("------2")
list=["3","4","5","6"]
print("_".join(list)) #将序列中的元素以指定字符串生成新的字符串

str2="abcedf"
print(str2.replace("bc", "kkk")) #替换字符串
str3="fsf,dksfjsl,fsldf"
print(str3.split(sep=","))#通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
str3="fsf\rDksfjsl\rfsldf"
print(str3.splitlines()) #按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符
print(str3.swapcase())  #将字符串大写转化为小写，小写转化为大写
