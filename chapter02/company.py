class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, index):
        return self.employee[index]


company = Company(['tom', 'bob', 'jane'])

for em in company:
    print(em)

# for 会一直调用，直到捕捉到异常
"""
tom
bob
jane
"""

print(company[:2])
"""
['tom', 'bob']
"""

# 这个我测试了：3.6.6 和 3.7.2 都不行
print(len(company))
"""
Traceback (most recent call last):
  File "company.py", line 26, in <module>
    print(len(company))
TypeError: object of type 'Company' has no len()
"""
