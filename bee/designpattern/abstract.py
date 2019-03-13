# coding=utf-8

"""
Abstract Factory
"""

import random


class PetShop(object):
    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print "this is lovely", str(pet)
        print "it says", pet.speak()
        print "it eats", self.pet_factory.get_food()


class Dog(object):
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat(object):
    def speak(self):
        return "miaomiao"

    def __str__(self):
        return "Cat"


class DogFactory(object):
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"


class CatFactory(object):
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"


def get_factory():
    return random.choice([DogFactory, CatFactory])()


if __name__ == "__main__":
    shop = PetShop()
    for i in range(5):
        shop.pet_factory = get_factory()
        shop.show_pet()
        print ('='*20)
