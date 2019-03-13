# coding=utf-8


class Context(object):
    def __init__(self):
        self.input=''
        self.output=""


class AbstractExpression(object):
    def Interpret(self, context):
        pass


class Expression(AbstractExpression):
    def Interpret(self, context):
        print "terminal interpret"


class NonterminalEepression(AbstractExpression):
    def Interpret(self, context):
        print "Nonterminal interpret"


if __name__ == '__main__':
    context = ""
    c = []
    c = c + [Expression()]
    c = c + [NonterminalEepression()]
    c = c + [Expression()]
    c = c + [Expression()]
    for a in c:
        a.Interpret(context)