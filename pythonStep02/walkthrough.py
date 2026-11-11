# Name: Aurora Tackett
# Date: 11/11/2026
# Program Name: walkthrough.py
# Description: Writing a program that follow's Mr. McMaster's example.

room = "Room 113"
seats = 24

print(room)
print(seats)

count = 5
count = count + 1
print(count)
print(type(count))

print(type("Ian Collins"))
print(type(3))
print(type(2.75))
print(type(True))
print(type("3"))


customer_name = "Carson Reynolds"
# Alternitively use 'customerName'
total_cost = 25

# Input asking for the user's first name. 
first_name = input("First Name: ")
last_name = input("Last Name: ")

# Output: greet them
print("Hello, " + first_name + " " + last_name + "!")

agetxt = input("Age: ")
agenum = int(agetxt)
print(agetxt)
print(agenum)
print(type(agetxt))
print(type(agenum))

ageNextYear = agenum + 1
print(ageNextYear)
print(type(ageNextYear))
ageNextYeartxt = str(ageNextYear)

print("You will be " + ageNextYeartxt + " next year!")

numberValue = input("Enter a float: ")
numberValue = float(numberValue)
print(type(numberValue))
print(numberValue)

numval = 4
numval = float(numval)
print(numval)

minutes = 135
hours = minutes // 60
leftover = minutes % 60
print(hours, "hours and", leftover, "minutes")

average = (16 + 16 + 17 + 16 + 17 + 16) / 6
print(average)
