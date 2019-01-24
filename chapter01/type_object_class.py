a = 1
b = 'abc'

# type -> int -> 1
# type -> str -> 'abc'
# type -> class -> obj
print(type(a))
print(type(int))
print(type(b))
print(type(str))
"""
<class 'int'>
<class 'type'>
<class 'str'>
<class 'type'>
"""

class Student:
    pass

class MyStudent(Student):
    pass

stu = Student()
print()
print(type(stu))
print(type(Student))
"""
<class '__main__.Student'>
<class 'type'>
"""

print()
print(int.__bases__)
print(str.__bases__)
"""
(<class 'object'>,)
(<class 'object'>,)
"""

print()
print(Student.__bases__)
print(MyStudent.__bases__)
"""
(<class 'object'>,)
(<class '__main__.Student'>,)
"""

print()
print(type.__bases__)
print(object.__bases__)
"""
(<class 'object'>,)
()
"""

print()
print(type(object))
print(type(type))
"""
<class 'type'>
<class 'type'>
"""

# object 是最顶层基类，object.__bases__ 得到一个空元组
# type 是一个类，同时 type 也是一个对象
