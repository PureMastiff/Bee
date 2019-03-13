# coding=utf-8


import time

class SaleManager(object):
    def work(self):
        print("Sales Manager working...")

    def talk(self):
        print("Sales Manager ready to talk")


class Proxy(object):
    def __init__(self):
        self.busy = "No"
        self.sales = None

    def work(self):
        print("Proxy checking for sales Managet availity")
        if self.busy == "No":
            self.sales = SaleManager()
            time.sleep(2)
            self.sales.talk()
        else:
            time.sleep(2)
            self.sales.work()
            print("Sales Manger is busy")


if __name__ == "__main__":
    p = Proxy()
    p.work()
    p.busy = 'Yes'
    p.work()

