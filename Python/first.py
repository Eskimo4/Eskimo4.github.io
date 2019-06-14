#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('''123
456
789''')
print(r'\n')

a = 999999999999999999999999999999999999999999999999999999999999999999999999999999
print(a)
a = a/9
print(a)
print("""--------------字符串编码---------------""")
#ASCII编码一个字节，只有英文和符号；UNICODE编码两个字节，UTF-8编码是变长字节(1-6)，包括各种语言。
#一般计算机内存中为UNICODE，存储和网络上用ASCII或UTF-8
print('爱你三千遍')
print(ord('A'),ord('中'))	#获取字符的十进制整数表示
print(chr(65),chr(20013))	#获取十进制整数表示的字符
#编码
print('ABC'.encode('ascii'))
print('ABC'.encode('utf-8'))
print('中文'.encode('utf-8'))	#在bytes中，无法显示为ASCII字符的字节，用\x##显示。
#解码
print(b'ABC'.decode('ascii'))
print(b'ABC'.decode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(b'\xe4\xb8\xad\xe6'.decode('utf-8',errors='ignore'))
#2个中文字符编码后为6个字节
print(len('中文'))
print(len('中文'.encode('utf-8')))
print("""--------------格式化输出--------------""")
print('int[%d]double[%.2f]char[%c]str[%s]'%(100,0.01,'a','abc'))	#%s永远起作用，它会把任何数据类型转换为字符串：
print('%d%%'% 7)
print('{0}%'.format(7))
print("""--------------list----------""")
mylist = ['abc','def']
print(mylist.append('xyz'))			#尾部添加
print(mylist.pop())					#尾部删除，并返回
print(mylist.insert(2,'xyz'))			#插入某位置
print(mylist.pop(2))					#删除某位置，并返回
mylist[1] = 123						#mylist可以存放各种类型，包括mylist
print(mylist,len(mylist),mylist[0],mylist[-1])
print("""--------------tuple-------------""")
tuple = ('abc','def')	#tuple不能被修改,没有append、insert等
#tuple[0] = 1			#不能对元素赋值
tuple = (123,)			#一个元素的tuple
print(tuple,len(tuple),tuple[0],tuple[-1])
tuple = ()				#空tuple
print("""--------------condition-------------""")
#year = input("input:")
#print(int(year) == 2019)

a = 0x100
a = 12.3e3
if a > 100:
	print(a)
else:
	print(100)
print("""----------Loop-----------""")
a=1
for i in range(1,23):
	a = a*i
print(a)
mylist = list(range(1,23))
print(mylist)

j,sum=1,0
while j<101:
	sum += j
	j+=2
print(sum)
print("""----------Dict 字典-------------""")
d = {"a":1,2:"b"}
d['c']=3
print(d,d['a'])
if 'd' in d:
	print(d['d'])
else:
	print("key not exist")
print(d.get('d'))

d.pop('c')
print(d.get('c',-1))
#Set和Dict的key都是不重复的,且必须是不可变对象
print("""-----------Set 无序集合-------------""")
s = set(['a','b','c'])
print(s)
s.add('d')
s.remove('a')
for ch in s:
	print(ch)
s2 = set(['c','x'])
s2.add(tuple)
t2 = ('0',['1','2'])
#s2.add(t2)
#集合的交集、并集、异或集运算
print(s & s2)
print(s | s2)
print(s ^ s2)
print("""---------------------------""")

