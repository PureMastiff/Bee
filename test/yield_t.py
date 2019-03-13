# coding=utf-8


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return



if __name__=='__main__':
    # f = fab(5)
    # print f.next()
    # print f.next()
    # print f.next()
    # print f.next()
    # print f.next()
    r = read_file('/Users/guogx/Desktop/windows.txt')
    for i in r:
        print i