#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 20:50:01 2018

@author: TenleySablatzky
"""
print("Let's start by getting to know you a little bit.")

Gender = input("Please select one: M/F or type N for nonbinary ")
str.capitalize("n", "m", "f")
if Gender == "1":
    bmrFemale = (655.0 + (4.35 * float(Weight)) + (4.7 * float(Height)) - 
    +(4.7 * float(Age))
    calorieIntake1 = bmrFemale * activityLevel
    print(calorieIntake1)
if Gender == "2":
    bmrMale = 66 + (6.23 * float(Weight)) + (12.7 * float(Height)) - 
    (6.8 * float(Height))
    calorieIntake2 = bmrMale * activityLevel
    print(calorieIntake2)      

Age = input("Enter your age numberically: ")
# Error control make sure a number is entered
try:
   val = int(Age)
except ValueError:
   print("That's not a number!")

Weight = input("What is your current weight in pounds? ")
# Error control/make sure a number is entered
try:
   val = int(Weight)
except ValueError:
   print("That's not a number!")

print("Input your height: ")
H_feet = int(input("Feet: "))
try:
   val = int(H_feet)
except ValueError:
   print("That's not a number!")
H_inch = int(input("Inches: "))
try:
   val = int(H_inch)
except ValueError:
   print("That's not a number!")
H_inch += H_feet * 12

Height = [H_inch, H_feet]

User = []
User = [Gender, Age, Weight, Height]
