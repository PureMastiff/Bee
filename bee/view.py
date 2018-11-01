# coding=utf-8
from os.path import dirname,realpath

def show(tree_info):
    print dirname(realpath(__file__))
    count_t = len(tree_info)
    for k,v in tree_info.items():
        count = len(v)
        count_t -= 1
        islast = 1 if not count_t else 0
        if islast:
            print '  └── {}'.format(k)
            for i in v:
                count -= 1
                islastone = 1 if not count else 0
                if islastone:
                    print '{}  └── {}'.format('     ',i)
                else:
                    print '{}  ├── {}'.format('     ',i)
        else:
            print '  ├── {}'.format(k)
            for i in v:
                count -= 1
                islastone = 1 if not count else 0
                if islastone:
                    print '{}  └── {}'.format('  │  ',i)
                else:
                    print '{}  ├── {}'.format('  │  ',i)