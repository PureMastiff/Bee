# coding=utf-8

def get():
    def al(x):
        return x*x*x
    return [al(x) for x in range(1,5)]
print get()