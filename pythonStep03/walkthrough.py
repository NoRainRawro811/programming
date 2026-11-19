# Name: Aurora Tackett 
# Date: 11/19/2026 
# Project Name: walkthrough.py
# Description: A walkthrough the professor is doing for our learning Python. 
age = 16 
print(age >=16) 
print(age <=16)
print(age == 16)
print(age != 18)

# Backspace 1 

score = int(input("Score: "))

if score >= 90:
    print(f"Your grade is A")
    grade = "A"
elif score >= 80:
    print(f"Your grade is B")
    grade = "B"
elif score >= 70:
    print(f"Your grade is C")
    grade = "C"
elif score >= 60:
    print(f"Your grade is D")
    grade = "D"
else:
    print(f"You got an F.")
    grade = "F"

print(f"The score you entered is {score}")
print(f"This means your grade is: {grade}")

# Backspace 2 

age = int(input("Age: "))

if age < 0 or age > 120:
    print("Error: age is unlikely. The range is 0 to 120.")
elif age >= 13 and age <= 19:
    print("You are a teenager.")
else:
    print("You are not a teenager.")


# Backspace 3 

day = input("Day of the week: ")

if day.lower() == "tuesday": 
    print("Half-price day!")
else: 
    print("Please check your spelling, otherwise, it's regular price day.")

print(day.lower())


# Backspace 4 


total = 11.00 

day = input("Day: ")
three_d = input("3D? (y/n): ")
popcorn = input("Popcorn? (y/n): ")

if day.lower() == "tuesday": 
    total = total - 3.00 
if three_d.lower() == "y":
    total = total + 2.50
if popcorn.lower() == "y":
    total = total + 0.99


print(f"Total: ${total:.2f}")


# Backspace 5 


day = input("Day of the week: ") 

day = day.lower() 

print(day)