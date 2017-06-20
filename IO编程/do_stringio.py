Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
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
>>> 
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
>>> 
