# coding = utf-8


try:
    res = 3/0
    mylist = [4, 6]
    print mylist[10]
    print 'this is never been called'
except ZeroDivisionError as e:
    print "Exception happen"
    print e
finally:
    print "Process finished"