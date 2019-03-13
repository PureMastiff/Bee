# coding=utf-8

import os


class Dog(object):
    def __init__(self):
        self.name = "dog"

    def bark(self):
        return 'woof'


class Cat(object):
    def __init__(self):
        self.name = "cat"

    def meow(self):
        return "miaomiao"


class Human(object):
    def __init__(self):
        self.name = "human"

    def speak(self):
        return "Hello"


class Car(object):
    def __init__(self):
        self.name = "car"

    def make_noise(self, oct_level):
        return "vroom {}".format(oct_level)


class Adapter(object):
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, item):
        return getattr(self.obj, item)


def main():
    objects = []
    dog = Dog()
    objects.append(Adapter(dog, dict(make_noise=dog.bark)))
    cat = Cat()
    objects.append(Adapter(cat, dict(make_noise=cat.meow)))
    human = Human()
    objects.append(Adapter(human, dict(make_noise=human.speak)))
    car = Car()
    car_noise = lambda: car.make_noise(3)
    objects.append(Adapter(car, dict(make_noise=car_noise)))

    for obj in objects:
        print "A", obj.name , "goes", obj.make_noise()


if __name__ == "__main__":
    main()
