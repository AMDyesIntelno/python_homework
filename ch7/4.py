#!/usr/bin/python3
# -*- coding: UTF-8
a=1
b=0
assert b!=0,"被除数不能为0"
print(a/b)
#AssertionError: 被除数不能为0
'''
➜  python_homework git:(master) ✗ python ch7/4.py
Traceback (most recent call last):
  File "ch7/4.py", line 5, in <module>
    assert b!=0,"被除数不能为0"
AssertionError: 被除数不能为0
➜  python_homework git:(master) ✗ python -O ch7/4.py
Traceback (most recent call last):
  File "ch7/4.py", line 6, in <module>
    print(a/b)
ZeroDivisionError: integer division or modulo by zero
'''