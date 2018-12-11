#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 20:50:01 2018

@author: TenleySablatzky
"""
print("Let's start by getting to know you a little bit.")

Gender = input("Please select one: Male: 1, Female: 2. Nonbinary: 3 ")
str.capitalize("n", "m", "f")     ### Am I using capitilize correctly? I get an error when I run.
if Gender == "1":
    bmrFemale = (655.0 + (4.35 * float(Weight)) + (4.7 * float(Height)) - 
    +(4.7 * float(Age))
    calorieIntake1 = bmrFemale * activityLevel  ### I'm getting an invalid syntax error around here. I'm sure it's 
    print(calorieIntake1)                       ### something obvious, I'm just not sure what to change.
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
