'''
Created on Dec 26, 2018

@author: user
'''
from datetime import datetime

class MyDog:
    home_address='300 Manhattan'
    def __init__ (self, breed, name, age, color):
        self.breed=breed
        self.name=name
        self.age=age
        self.color=color
        self.isAsleep=False

    def walk(self):
        print("{} is walking!".format(self.name))
    def eat(self,food):
        print("{} is eating a {}!".format(self.name,food))
    def sleep(self):
        self.isAsleep=True
        print("{} is sleeping!".format(self.name))
    def wake_up(self):
        self.isAsleep=False
        print("{} is waking up!".format(self.name))
    def info(self):
        print("My dog is a {}, named {}. My dog is {} years old and has {} fur. We live in {}.".format(self.breed,self.name, self.age, self.color, self.home_address))
    
    
    @classmethod
    def from_birthyear(cls, breed, name, birthyear, color):
        age=datetime.now().year - birthyear
        return cls(breed, name, age, color)
    @classmethod
    def move(cls,destination):
        cls.home_address=destination
        print("We moved to {}!".format(cls.home_address))
        
    @staticmethod
    def checkup_needed(age):
        return (age-1)%3==0
