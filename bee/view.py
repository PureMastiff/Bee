# coding=utf-8


def show(tree_info):
    for k,v in tree_info.items():
        count = len(v)
        print '{} ({})'.format(k, count)
        for i in v:
            count -= 1
            islastone = 1 if not count else 0
            if islastone:
                print '   └── {}'.format(i)
            else:
                print '   ├── {}'.format(i)