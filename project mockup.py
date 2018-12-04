# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:14:07 2018

@author: MoLeigh
"""

# TO DO
#1. collect the demographic info from the user. --> input() store in 
# variables/lists/dictionaries
#2. define daily recommended calorie intake based on the data they gave you 
#and information from the web --> math formulas to calculate
#3. allow a user to enter information about one meal --> input() store in 
# variables/lists/dictionaries
#4. calculate the number of calories from that meal (based on some info 
# available online) --> JSON/CSV data from the web (some info source) that 
# allows you to search for what you are looking for and retrieve appropriate 
# information


# Collect Gender, Age, Weight, Height
# Covert height to inches
# Use Harris-Benedict Formula to calcuate calore intake
# http://www.healthfitonline.com/resources/harris_benedict.php
# Calculate BMR
# Calculate Calories
# Print Calorie Intake Result to Screen


#    uSedentary = 1.2
#    uLightActivity = 1.375
#    uModerateActivity = 1.55
#    uVeryActive = 1.725
#    uExtraActive = 1.9

# A = 1.2 
# B = 1.375 
# C = 1.55 
# D = 1.725
# E = 1.9


# Collect Level of Activity
#for x in activityLevel:
activityInput = input("Please select type in the letter that corresponds "
                          "to your activity level:\n"
                          "A for sedentary\n"
                          "B for lightly active\n" 
                          "C moderately active\n" 
                          "D very active\n"
                          "E extra active\n")


if activityInput == "A":
    activityLevel = 1.2
    
elif activityInput == "B":
    activityLevel = 1.375

elif activityInput == "C":
    activityLevel = 1.55

elif activityInput == "D":
    activityLevel = 1.725

elif activityInput == "E": 
    activityLevel = 1.9     
    
# Convert activityInput to uppercase
#    if activityInput in activityLevel:
#        print("You entered: ", activityInput)
    
# Insert try/catch to make sure 1 or 2 is entered
uGender = input("Enter 1 for Female or 2 for Male: ")    

# Validate input - must be a double or int
uWeight = input("How much do you weigh?: ")
# Insert try/catch to make sure a number is entered
# Insert try/catch to make sure number is between 0 and 1000
 
# Validate input - must be an int
uAge = input("Age: ")
# Insert try/catch to make sure a number is entered
# Insert try/catch to make sure the number is between 1 and 120
# Validate input - must be 1 or 2

# validate input - can be inches or feet and inches
uHeight = input("Enter your height: ")
# convert height to inches


# Collect gender
if uGender == "1":
    bmrFemale = 655.0 + (4.35 * float(uWeight)) + (4.7 * float(uHeight)) - (4.7 * float(uAge))
    calorieIntake1 = bmrFemale * activityLevel
    print(calorieIntake1)
if uGender == "2":
    bmrMale = 66 + (6.23 * float(uWeight)) + (12.7 * float(uHeight)) - (6.8 * float(uHeight))
    calorieIntake2 = bmrMale * activityLevel
    print(calorieIntake2)            


# Collect foods eaten
# Match foods eaten with calories for each food
# Add calories
# Print Calories to Screen
# Subtract entered meals calories from day's calorie total