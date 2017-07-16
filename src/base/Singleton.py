'''
Created on 2017年7月16日

@author: Administrator
'''

# 实现方法1


class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_sgl"):
            cls._sgl = super().__new__(cls, *args, **kwargs)
        return cls._sgl


#'''实现方法2'''
def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class MySingleton():
    pass


if __name__ == '__main__':
    sa = MySingleton()
    sb = MySingleton()
    print(id(sa))
    print(id(sb))
