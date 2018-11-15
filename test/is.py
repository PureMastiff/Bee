# coding=utf-8
import copy

#深copy 浅copy
a = [11, 22, 33]
b = a

print(a==b)
#True
print(a is b)
#True

c = copy.deepcopy(a)

print(a==b)
#True
print(a is b)
#False