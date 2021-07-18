# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 11:13:41 2021

@author: kody
"""

class Pet:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age
        
    def show(self):
        print(f"i am {self.name} and i am {self.age} years old ")
        
    def speak(self):
        print("I dont know what to say")
        
        
class Cat(Pet):
    def speak(self):
        print("Meow")
        
class Dog(Pet):
    def speak(self):
        print("Bark")
        
        
p = Pet("Tim", 19)
p.speak()