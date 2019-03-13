# coding=utf-8

import copy
"""
    ProtoType
"""


class ProtoType(object):
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


def main():
    class A(object):
        def __str__(self):
            return "I am A"

    a = A()
    prototype = ProtoType()
    prototype.register_object('a', a)
    b = prototype.clone('a', b=2,c=3,a=1)

    print a
    print (b.a, b.b, b.c)


if __name__ == "__main__":
    main()