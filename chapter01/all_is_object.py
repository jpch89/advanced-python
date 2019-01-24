def ask(name='Jack'):
    print(name)


class Person:
    def __init__(self):
        print('Ma')

my_func = ask
my_func()
"""
Jack
"""

print()
my_class = Person
my_class()
"""
Ma
"""

print()
obj_list = []
obj_list.extend([ask, Person])
for item in obj_list:
    print(item())
"""
Jack
None
Ma
<__main__.Person object at 0x0000024556E5AC50>
"""

def decorator_func():
    print('dec start')
    return ask

print()
my_ask = decorator_func()
my_ask('Tom')
"""
dec start
Tom
"""
