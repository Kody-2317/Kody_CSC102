# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 14:55:14 2021

@author: kody
"""


import pandas

def sims():
    condition = int(input("Amount of Data:"))
    names = []
    departments = []
    levels = []
    matric_numbers =[]
    
    
    for a in range(condition):
        name = str(input("Input a name: "))
        names.append(name)
        department = str(input("Input department: "))
        departments.append(department)
        level = int(input("input level:"))
        levels.append(level)
        matric_number = int(input("Input Matric_no: "))
        matric_numbers.append(matric_number)
        print(".........")
        
    
    data = {"Name" : names, "Department": departments, "Level": levels, "MAtric Number": matric_numbers }
    
    Data_Frame = pandas.DataFrame(data)
    Data_Frame.to_excel("sims.xlsx")
    return Data_Frame



sims()