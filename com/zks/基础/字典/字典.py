# -*- coding: gbk -*-
'''
Created on 2017年5月5日
1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
2 ）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
@author: Administrator
'''
from email.policy import strict
from platform import dist


map={"zks":1,"kai":2,"shun":3}
#访问数据
print(map["zks"])
#修改数据
map["zks"]=8
print(map["zks"])

#删除字典数据
del map["zks"]  #删除键"zks"
map.clear()   #清空字典
del map    #清空字典
map={"zks":1,"kai":2,"shun":3}

