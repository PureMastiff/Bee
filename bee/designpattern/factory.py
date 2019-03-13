# coding=utf-8
# 参考链接：https://www.cnblogs.com/Liqiongyu/p/5916710.html
"""
Factory Method
"""


class ChinaGetter(object):
    def __init__(self):
        self.trans = dict(dog="小狗", cat="小猫")

    def get(self, msgid):
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)


class EnglishGetter(object):
    def get(self, msgid):
        return str(msgid)


def get_localizer(langauge="English"):
    langauges = dict(English=EnglishGetter, China=ChinaGetter)
    return langauges[langauge]()


e, g = get_localizer("English"), get_localizer("China")

for msgid in "dog parrot cat bear".split():
    print e.get(msgid), g.get(msgid)

