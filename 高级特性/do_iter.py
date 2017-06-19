Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> sum = 0
>>> for x in range(101):
	sum = sum + x
print(sun)
SyntaxError: invalid syntax
>>> print(sum)
0
>>> d = {'a':1,'b':2,'c':3}
>>> for key in d:
	print(key)

a
b
c
>>> for value in d.values:
	print(value)

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    for value in d.values:
TypeError: 'builtin_function_or_method' object is not iterable
>>> for value in d.values():
	print(value)

	
1
2
3
>>> 
>>> for k,v in d:
	print('{%s:%s}' %(k,v))

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    for k,v in d:
ValueError: not enough values to unpack (expected 2, got 1)
>>> for k,v in d.items():
	print('{%s:%s}' %(k,v))

{a:1}
{b:2}
{c:3}
>>> from collection import Iterable
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    from collection import Iterable
ModuleNotFoundError: No module named 'collection'
>>> from collections import Iterable
>>> isinstance('abc',Iterable)
True
>>> isinstance(123,Iterable)
False
>>> for i,value in enumerate(['A','B','C'])
SyntaxError: invalid syntax
>>> for i, value in enumerate(['A', 'B', 'C']):
	     print(i, value)

0 A
1 B
2 C
>>> for x, y in [(1,1),(2,4),(3,9)]
SyntaxError: invalid syntax
>>> for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x,y)

1 1
2 4
3 9
>>> 
