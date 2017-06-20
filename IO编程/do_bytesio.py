Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from io import BytesIO
>>> f = BytesIO()
>>> f.write('中文'.encode('utf-8'))
6
>>> printf(f.getva)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    printf(f.getva)
NameError: name 'printf' is not defined
>>> print(f.getvalue())
b'\xe4\xb8\xad\xe6\x96\x87'
>>> 
>>> from io import BytesIO
>>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
>>> f.read()
b'\xe4\xb8\xad\xe6\x96\x87'
>>> 
