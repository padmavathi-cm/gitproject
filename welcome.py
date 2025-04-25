Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> welcome():
...     
SyntaxError: invalid syntax
>>> welcome()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    welcome()
NameError: name 'welcome' is not defined
>>> class welcome:
...     print ('hi all')
