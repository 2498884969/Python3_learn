Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> f = open('test.txt','r')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    f = open('test.txt','r')
FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
>>> f = open('D:\编程\Python3_learn\IO编程\test.txt')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    f = open('D:\编程\Python3_learn\IO编程\test.txt')
OSError: [Errno 22] Invalid argument: 'D:\\编程\\Python3_learn\\IO编程\test.txt'
>>> f = open('D:/编程/Python3_learn/IO编程/test.txt')
>>> f.read()
'娴嬭瘯\n'
>>> f.read()
''
>>> f.close
<built-in method close of _io.TextIOWrapper object at 0x02DEEC30>
>>> try:
	f = open('/path/to/file','r')
	print(f.read())
finally:
	if f:
		f.close()

Traceback (most recent call last):
  File "<pyshell#12>", line 2, in <module>
    f = open('/path/to/file','r')
FileNotFoundError: [Errno 2] No such file or directory: '/path/to/file'
>>> with open('/path/to/file','r') as f:
	print(f.read())


Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    with open('/path/to/file','r') as f:
FileNotFoundError: [Errno 2] No such file or directory: '/path/to/file'
>>>
