class A:
    pass


class B(A):
    pass


b = B()

print(isinstance(b, B))
print(isinstance(b, A))
"""
True
True
"""

print()
print(type(b))
print(type(b) is B)
print(type(b) is A)
"""
<class '__main__.B'>
True
False
"""

# isinstance 会在继承链里面寻找
# 而 type 不会
