Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.name
'nt'
>>> os.uname()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    os.uname()
AttributeError: module 'os' has no attribute 'uname'
>>> os.en
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    os.en
AttributeError: module 'os' has no attribute 'en'
>>> os.environ
environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\dell\\AppData\\Roaming', 'CM2014DIR': 'C:\\Program Files (x86)\\Common Files\\Autodesk Shared\\Materials\\', 'COMMONPROGRAMFILES': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DELL-PC', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'CRX_PATH_2013_X86': 'D:\\办公软件\\caxa\\caxa2013\\2013\\CRX\\', 'FP_NO_HOST_CHECK': 'NO', 'HOME': 'C:\\Users\\dell', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\dell', 'ILBDIR': 'C:\\Program Files (x86)\\Common Files\\Autodesk Shared\\Materials\\', 'INTEL_LICENSE_FILE': 'C:\\Program Files (x86)\\Common Files\\Intel\\Licenses', 'JAVA_HOME': 'D:\\coding\\JAVA\\jdk', 'LOCALAPPDATA': 'C:\\Users\\dell\\AppData\\Local', 'LOGONSERVER': '\\\\DELL-PC', 'NUMBER_OF_PROCESSORS': '4', 'OS': 'Windows_NT', 'PATH': 'D:\\coding\\JAVA\\jdk\\bin;C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Python27\\Scripts;C:\\Program Files\\Common Files\\Siemens\\Automation\\Simatic OAM\\bin;D:\\coding\\Qt\\Qt\\5.5\\msvc2013\\bin;C:\\Program Files (x86)\\Intel\\iCLS Client\\;C:\\Program Files\\Intel\\iCLS Client\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\Microsoft SQL Server\\110\\Tools\\Binn\\;C:\\Program Files (x86)\\Windows Kits\\8.1\\Windows Performance Toolkit\\;C:\\Program Files\\nodejs\\;C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36-32\\Scripts\\;C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36-32\\;D:\\办公软件\\cmake-3.7.0\\bin;C:\\Program Files (x86)\\Microsoft VS Code\\bin;C:\\Users\\dell\\AppData\\Roaming\\npm', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'x86', 'PROCESSOR_ARCHITEW6432': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 94 Stepping 3, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '5e03', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files (x86)', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\', 'PUBLIC': 'C:\\Users\\Public', 'SESSIONNAME': 'Console', 'SIMATIC_OAM': 'C:\\Program Files\\Common Files\\Siemens\\Automation\\Simatic OAM', 'SIMATIC_OAM_DATA': 'C:\\ProgramData\\Siemens\\Automation\\Simatic OAM', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\dell\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\dell\\AppData\\Local\\Temp', 'USERDOMAIN': 'dell-PC', 'USERNAME': 'dell', 'USERPROFILE': 'C:\\Users\\dell', 'VS120COMNTOOLS': 'D:\\编程\\vs2013\\vs2013\\Common7\\Tools\\', 'WINDIR': 'C:\\Windows', 'WINDOWS_TRACING_FLAGS': '3', 'WINDOWS_TRACING_LOGFILE': 'C:\\BVTBin\\Tests\\installpackage\\csilogfile.log'})
>>> environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\dell\\AppData\\Roaming', 'CM2014DIR': 'C:\\Program Files (x86)\\Common Files\\Autodesk Shared\\Materials\\', 'COMMONPROGRAMFILES': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DELL-PC', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'CRX_PATH_2013_X86': 'D:\\办公软件\\caxa\\caxa2013\\2013\\CRX\\', 'FP_NO_HOST_CHECK': 'NO', 'HOME': 'C:\\Users\\dell', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\dell', 'ILBDIR': 'C:\\Program Files (x86)\\Common Files\\Autodesk Shared\\Materials\\', 'INTEL_LICENSE_FILE': 'C:\\Program Files (x86)\\Common Files\\Intel\\Licenses', 'JAVA_HOME': 'D:\\coding\\JAVA\\jdk', 'LOCALAPPDATA': 'C:\\Users\\dell\\AppData\\Local', 'LOGONSERVER': '\\\\DELL-PC', 'NUMBER_OF_PROCESSORS': '4', 'OS': 'Windows_NT', 'PATH': 'D:\\coding\\JAVA\\jdk\\bin;C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Python27\\Scripts;C:\\Program Files\\Common Files\\Siemens\\Automation\\Simatic OAM\\bin;D:\\coding\\Qt\\Qt\\5.5\\msvc2013\\bin;C:\\Program Files (x86)\\Intel\\iCLS Client\\;C:\\Program Files\\Intel\\iCLS Client\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\Microsoft SQL Server\\110\\Tools\\Binn\\;C:\\Program Files (x86)\\Windows Kits\\8.1\\Windows Performance Toolkit\\;C:\\Program Files\\nodejs\\;C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36-32\\Scripts\\;C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36-32\\;D:\\办公软件\\cmake-3.7.0\\bin;C:\\Program Files (x86)\\Microsoft VS Code\\bin;C:\\Users\\dell\\AppData\\Roaming\\npm', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'x86', 'PROCESSOR_ARCHITEW6432': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 94 Stepping 3, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '5e03', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files (x86)', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\', 'PUBLIC': 'C:\\Users\\Public', 'SESSIONNAME': 'Console', 'SIMATIC_OAM': 'C:\\Program Files\\Common Files\\Siemens\\Automation\\Simatic OAM', 'SIMATIC_OAM_DATA': 'C:\\ProgramData\\Siemens\\Automation\\Simatic OAM', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\dell\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\dell\\AppData\\Local\\Temp', 'USERDOMAIN': 'dell-PC', 'USERNAME': 'dell', 'USERPROFILE': 'C:\\Users\\dell', 'VS120COMNTOOLS': 'D:\\编程\\vs2013\\vs2013\\Common7\\Tools\\', 'WINDIR': 'C:\\Windows', 'WINDOWS_TRACING_FLAGS': '3', 'WINDOWS_TRACING_LOGFILE': 'C:\\BVTBin\\Tests\\installpackage\\csilogfile.log'})
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\dell\\AppData\\Roaming', 'CM2014DIR': 'C:\\Program Files (x86)\\Common Files\\Autodesk Shared\\Materials\\', 'COMMONPROGRAMFILES': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DELL-PC', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'CRX_PATH_2013_X86': 'D:\\办公软件\\caxa\\caxa2013\\2013\\CRX\\', 'FP_NO_HOST_CHECK': 'NO', 'HOME': 'C:\\Users\\dell', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\dell', 'ILBDIR': 'C:\\Program Files (x86)\\Common Files\\Autodesk Shared\\Materials\\', 'INTEL_LICENSE_FILE': 'C:\\Program Files (x86)\\Common Files\\Intel\\Licenses', 'JAVA_HOME': 'D:\\coding\\JAVA\\jdk', 'LOCALAPPDATA': 'C:\\Users\\dell\\AppData\\Local', 'LOGONSERVER': '\\\\DELL-PC', 'NUMBER_OF_PROCESSORS': '4', 'OS': 'Windows_NT', 'PATH': 'D:\\coding\\JAVA\\jdk\\bin;C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Python27\\Scripts;C:\\Program Files\\Common Files\\Siemens\\Automation\\Simatic OAM\\bin;D:\\coding\\Qt\\Qt\\5.5\\msvc2013\\bin;C:\\Program Files (x86)\\Intel\\iCLS Client\\;C:\\Program Files\\Intel\\iCLS Client\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\Microsoft SQL Server\\110\\Tools\\Binn\\;C:\\Program Files (x86)\\Windows Kits\\8.1\\Windows Performance Toolkit\\;C:\\Program Files\\nodejs\\;C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36-32\\Scripts\\;C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36-32\\;D:\\办公软件\\cmake-3.7.0\\bin;C:\\Program Files (x86)\\Microsoft VS Code\\bin;C:\\Users\\dell\\AppData\\Roaming\\npm', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'x86', 'PROCESSOR_ARCHITEW6432': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 94 Stepping 3, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '5e03', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files (x86)', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\', 'PUBLIC': 'C:\\Users\\Public', 'SESSIONNAME': 'Console', 'SIMATIC_OAM': 'C:\\Program Files\\Common Files\\Siemens\\Automation\\Simatic OAM', 'SIMATIC_OAM_DATA': 'C:\\ProgramData\\Siemens\\Automation\\Simatic OAM', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\dell\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\dell\\AppData\\Local\\Temp', 'USERDOMAIN': 'dell-PC', 'USERNAME': 'dell', 'USERPROFILE': 'C:\\Users\\dell', 'VS120COMNTOOLS': 'D:\\编程\\vs2013\\vs2013\\Common7\\Tools\\', 'WINDIR': 'C:\\Windows', 'WINDOWS_TRACING_FLAGS': '3', 'WINDOWS_TRACING_LOGFILE': 'C:\\BVTBin\\Tests\\installpackage\\csilogfile.log'})
NameError: name 'environ' is not defined
>>> os.environ('path')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    os.environ('path')
TypeError: '_Environ' object is not callable
>>> os.environ.get('Path')
'D:\\coding\\JAVA\\jdk\\bin;C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Python27\\Scripts;C:\\Program Files\\Common Files\\Siemens\\Automation\\Simatic OAM\\bin;D:\\coding\\Qt\\Qt\\5.5\\msvc2013\\bin;C:\\Program Files (x86)\\Intel\\iCLS Client\\;C:\\Program Files\\Intel\\iCLS Client\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\Microsoft SQL Server\\110\\Tools\\Binn\\;C:\\Program Files (x86)\\Windows Kits\\8.1\\Windows Performance Toolkit\\;C:\\Program Files\\nodejs\\;C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36-32\\Scripts\\;C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36-32\\;D:\\办公软件\\cmake-3.7.0\\bin;C:\\Program Files (x86)\\Microsoft VS Code\\bin;C:\\Users\\dell\\AppData\\Roaming\\npm'
>>> os.path.abspath('.')
'C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python36-32'
>>> os.path.join('D:/编程','testdir')
'D:/编程\\testdir'
>>> os.mkdir('D:/编程')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    os.mkdir('D:/编程')
FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: 'D:/编程'
>>> os.mkdir('D:/编程/testdir')
>>> os.rmdir('D:/编程/testdir')
>>> os.path.join('D:/编程','testdir')
'D:/编程\\testdir'
>>> os.mkdir('D:/编程/testdir')
>>> os.path.join('D:/编程/testdir','test.txt')
'D:/编程/testdir\\test.txt'
>>> os.mkdir('D:/编程/testdir/test.txt')
>>> f = fopen('D:/编程/testdir/test.txt','w')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    f = fopen('D:/编程/testdir/test.txt','w')
NameError: name 'fopen' is not defined
>>> f = open('D:/编程/testdir/test.txt','w')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    f = open('D:/编程/testdir/test.txt','w')
PermissionError: [Errno 13] Permission denied: 'D:/编程/testdir/test.txt'
>>> f = open('D:/编程/testdir/nihao.txt','w')
>>> os.path.split('D:/编程/testdir/nihao.txt')
('D:/编程/testdir', 'nihao.txt')
>>> os.path.splitext('D:/编程/testdir/nihao.txt')
('D:/编程/testdir/nihao', '.txt')
>>> os.rename('test.txt','test.py')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    os.rename('test.txt','test.py')
FileNotFoundError: [WinError 2] 系统找不到指定的文件。: 'test.txt' -> 'test.py'
>>> os.curdir
'.'
>>> os.chdir('D:/编程/testdir')
>>> os.rename('test.txt','test.py')
>>> import shutil
>>> os.getcwd()
'D:\\编程\\testdir'
>>> shutil.copyfile('test.py','test2.py')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    shutil.copyfile('test.py','test2.py')
  File "C:\Users\dell\AppData\Local\Programs\Python\Python36-32\lib\shutil.py", line 114, in copyfile
    with open(src, 'rb') as fsrc:
PermissionError: [Errno 13] Permission denied: 'test.py'
>>> shutil.copyfile('D:/编程/testdir/nihao.txt','D:/编程/testdir/nihao1.txt')
'D:/编程/testdir/nihao1.txt'
>>> [x for x in x in os.listdir('.') if os.path.isdir(x)]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    [x for x in x in os.listdir('.') if os.path.isdir(x)]
NameError: name 'x' is not defined
>>> [x for x in os.listdir('.') if os.path.isdir(x)]
['test.py']
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext[1]=='.text']
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext[1]=='.text']
  File "<pyshell#32>", line 1, in <listcomp>
    [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext[1]=='.text']
TypeError: 'function' object is not subscriptable
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
[]
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.txt']
['nihao.txt', 'nihao1.txt']
>>> 
