# coding=utf-8

"""
    Singleton
"""


class SingleTon(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            org = super(SingleTon, cls)
            cls._instance = org.__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    class SingleSpam(SingleTon):
        def __init__(self, s):
            self.s = s

        def __str__(self):
            return self.s

    s1 = SingleSpam('spam')
    # id() 函数获取对象的内内存地址
    print id(s1), s1
    s2 = SingleSpam('spa')
    print id(s2), s2
    print id(s1), s1