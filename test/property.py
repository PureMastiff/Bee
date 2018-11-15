# coding=utf-8

class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error: 不是整型数字")

    @property
    def money(self):
        return self.__money


    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error: 不是整型数字")


t = Money()
a = t.money
print a
t.money = 100
print t.money

t.setMoney("21a")
t.setMoney(22)
print t.getMoney()