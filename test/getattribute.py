# coding=utf-8


class Itcast(object):
    def __init__(self, subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'

    def __getattribute__(self, obj):
        print '1111111'
        if obj == 'subject1':
            print('log subject1')
            return 'redirect python'
        else:
            print '22222222'
            return object.__getattribute__(self, obj)

    def show(self):
        print('this is Itcast')


class Person(object):
    def __getattribute__(self,obj):
        print("---test---")
        if obj.startswith("a"):
            return "hahha"
        else:
            return self.test
    def test(self):
        print("heihei")


s = Itcast('python')

print s.subject1
print s.subject2
print s.show()


t = Person()
print t.a
print t.b