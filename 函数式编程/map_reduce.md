Python内建了map()和reduce()函数。
### map
我们先来看map。map()函数接收两个参数，一个是函数，一个是iterable,map将传入的函数依次作用到每个序列的每个元素，并把结果作为新的Iterator返回。

举例说明，比如我们有一个函数f(x)=x*x,要把函数作用在一个list[1,2,3,4,5,6,7,8,9]上，就可以用map()实现如下：
![](0.png)
```Python
>>> r = map(f,[1,2,3,4,5,6,7,8,9])
>>> r
<map object at 0x00236CB0>
>>> next(r)
1
>>> list(r)
[4, 9, 16, 25, 36, 49, 64, 81]
```
### reduce
再看reduce的用法。reduce把一个函数作用在一个序列[x1,x2,x3,...]这个函数必须接受两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
```Python
reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)
```

比如，对于一个序列求和：
```Python
>>> from functools import reduce
>>> def add(x,y):
	return x+y

>>> reduce(add,[1,3,5,7,9])
25
>>> def fn(x,y):
	return x*10+y

>>> reduce(fn,[1,3,5,7,9])
13579
```
字符串转数字
```Python
>>> def str2int(s):
	def fn(x,y):
		return x*10 +y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn,map(char2num,s))

>>> str2int('13579')
13579
>>> def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

>>> def str3int(s):
	return reduce(lambda x,y:x * 10 + y,map(char2num,s))

>>> str3int('13579')
13579
```
人名格式转化
```Python
>>> def normalize(name):
	return name.capitalize()

>>> map(normalize,['adam','LISA','barT'])
<map object at 0x02E8CC10>
>>> list(map(normalize,['adam','LISA','barT']))
['Adam', 'Lisa', 'Bart']

```
求序列之积
```Python
>>> from functools import reduce
>>> def prod(L):
	return reduce(lambda x,y:x*y,L)

>>> prod([1,2,3,4,5,6])
720
```
