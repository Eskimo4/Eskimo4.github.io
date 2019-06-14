#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""--------------函数---------------""")
print(max(1,324,12123,43534))
mymax = max
print(mymax(1,2))

#十进制转换成十六进制表示
print(hex(255))
f = 255.0
print(f.hex())	#这种调用不适用整数，只能浮点数，why？？？

def circle(r,pi=3.14):
	#参数类型检查
	if not isinstance(r,(int,float)):
		raise TypeError("bad operand type")
	pass
#没有return时函数返回None
	return pi*r*r,r
#通过返回一个tuple的方式，获取多个返回值
area,r = circle(1,3)
print(area,r)

opr = 123
if not isinstance(opr,(int,float)):
	print("opr is not int or float")
else:
	print('opr is int or float')

x,y = (123,'abc')
print(x,y)

#默认参数必须是不可变对象
def default(l=[]):
	l.append('end');
	print(l)
default()
default()

#可变参数,自动组成tuple作为入参
def cal(*nums):
	sum = 0
	for num in nums:
		sum += num
	print(sum)
cal()
cal(1,2,3)
numlist = [1,2,3]
cal(*numlist)

#关键字参数，自动组成dict作为入参
def keyvalue(**kvs):
	print(kvs)
keyvalue()
keyvalue(a=1,b=2)
kvdict = {"a":1,"b":2}
keyvalue(**kvdict)

#命名关键字参数,为了限制调用者可以传入的参数名，同时可以提供默认值
def name(*,d,e='ABC'):
	print(d,e)
name(d='abc')

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

#使用尾递归可以使编译器或解释器可以对函数调用栈做优化，以防止过深的递归导致栈溢出
def fact(n,res=1):
	if n<2:
		return res
	res = res*n
	return fact(n-1,res)
print(fact(5))
#遗憾的是，python解释器并没有优化，emmmmmmm
#print(fact(1000))