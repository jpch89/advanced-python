class A:
    aa = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = A(2, 3)
A.aa = 11
a.aa = 100  # 在对象上新建变量 aa
print(a.x, a.y, a.aa)
print(A.aa)
"""
2 3 100
11
"""

print()
b = A(3, 5)
print(b.aa)  # 类变量被所有实例共享
"""
11
"""
