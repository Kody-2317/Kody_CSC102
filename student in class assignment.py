# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 14:19:55 2021

@author: kody
"""

class Student:
     studentLevel = 'first year computer science 2020/2021 session'
     studentCounter = 0
     def __init__(self, thename, thematricno, thesex, thehostelname, theage, thecsc102examscore):
         self.name = thename
         self.matricno = thematricno
         self.sex = thesex
         self.age = theage
         self.hostelname = thehostelname
         self.csc102score = thecsc102examscore
         Student.studentCounter = Student.studentCounter

     def getName(self):
         return  self.name

     def setName(self, thenewName):
         self.name = thenewName
    
     def agechecker(self, theage):
        if (self.age > 16):
            return self.age
        else:
            print("Student not up to 16")
    
     def registeredcourse(self, thecsc102examscore):
         print("registered course is CSC102")
         
     def scorechecker(self, thecsc102examscore):
         if (self.csc102score < 45):
             print ("Please you would have to re-enrol for this course next year")
         else:
             print(f"you passed csc102 your score is{self.csc102score}")
             
     @staticmethod 
     def numtype(a):
        if a/2 == 0:
            print("This is an even number")
        else:
            print("This is an odd number")
        
student1 = Student('James Kaka', '021074', 'M', "Faith hostel", 15, 27 )

student1.numtype(17)