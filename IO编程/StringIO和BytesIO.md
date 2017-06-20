### StringIO
很多事后数据读写不一定是文件，也可以在内存中读写。

StringIO就是在内存中读写str。
```Python
>>> from io import StringIO
>>> f = StringIO()
>>> f.write('hello')
5
>>> f.write(' ')
1
>>> f.write('world')
5
>>> print(f.getvalue())
hello world
```
getvalue()方法用于获得写入后的str。

要读取StringIO,可以用一个str初始化stringio，然后想读文件一样读取：
```Python
>>> from io import StringIO
>>> f = StringIO('Hello\nHi!\nGoodbye!')
>>> while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())


Hello
Hi!
Goodbye!
```
### BytesIO
```Python
>>> from io import BytesIO
>>> f = BytesIO()
>>> f.write('中文'.encode('utf-8'))
6
>>> print(f.getvalue())
b'\xe4\xb8\xad\xe6\x96\x87'

>>> from io import BytesIO
>>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
>>> f.read()
b'\xe4\xb8\xad\xe6\x96\x87'
```
