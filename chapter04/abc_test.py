# 检查某个类是否有某种方法
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, index):
        return self.employee[index]

    def __len__(self):
        return len(self.employee)


# hasattr 判断某个对象是否有某个属性
print(hasattr(Company, '__len__'))
"""
True
"""

# 我的方法：检查属性字典
print()
print('__len__' in Company.__dict__)
"""
True
"""

# 如果不使用 isinstance，就要用 hasattr 或者判断属性字典的键，这样很麻烦
from collections.abc import Sized
print()
print(isinstance(Company(['Patrick', 'Jane']), Sized))
"""
True
"""

# 我们在某些情况之下希望判定某个对象的类型
# 我们需要强制某个子类必须实现某些方法
# 比如实现了一个 web 框架
# 集成 cache（redis，cache，memorycache）
# 需要设计一个抽象基类，指定子类必须实现某些方法
class CacheBase:
    def get(self, key):
        raise NotImplementedError
    def set(self, key, value):
        raise NotImplementedError


class RedisCache(CacheBase):
    pass


# redis_cache = RedisCache()
# redis_cache.set('key', 'value')
"""
Traceback (most recent call last):
  File "abc_test.py", line 51, in <module>
    redis_cache.set('key', 'value')
  File "abc_test.py", line 43, in set
    raise NotImplementedError
NotImplementedError
"""

import abc
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass

class RedisCache(CacheBase):
    pass

redis_cache = RedisCache()  # 初始化的时候就可以抛出异常
"""
Traceback (most recent call last):
  File "abc_test.py", line 74, in <module>
    redis_cache = RedisCache()
TypeError: Can't instantiate abstract class RedisCache with abstract methods get, set
"""

