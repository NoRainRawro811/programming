from Funsies.functioning.funniFunctionsToNeverCall import amHateSpeech
# Name: Aurora Tackett
# Date: 11/13/2026
# Program: step03Tasks.py 
# Description: Every task neatly made into one coherent selectable and repeatable program. 

def error():
    print("If you're seeing this error text, one of us messed something up.")

def task1():
    # Name: Aurora Tackett
    # Date: 11/23/2026
    # Program: step03Tasks.py 
    # Description: Pass fail 
    score = int(input("Score: "))
    if score >= 70:
        print(f"Score: {score}\nYou passed.")
    else:
        print(f"Score: {score}\nYou did not pass.")


def task2():
    # Name: Aurora Tackett
    # Date: 11/23/2026
    # Program: step03Tasks.py 
    # Description: Even or odd
    num = int(input("[2]Enter a number: "))
    odev = num % 2
    if odev == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")


def task3():
    # Name: Aurora Tackett
    # Date: 11/23/2026
    # Program: step03Tasks.py 
    # Description: Pos/neg/zero 
    negnum = int(input("[3] Enter a number: "))
    if negnum > 0:
        print("Negative")
    elif negnum == 0:
        print("Zero")
    else:
        print("Positive")


def task4():
    # Name: Aurora Tackett
    # Date: 11/23/2026
    # Program: step03Tasks.py 
    # Description: grade 
    score = int(input("Score: "))
    if score >= 90:
        print(f"Score: {score}\nGrade: A")
        grade = "A"
    elif score >= 80:
        print(f"Score: {score}\nGrade: B")
        grade = "B"
    elif score >= 70:
        print(f"Score: {score}\nGrade: C")
        grade = "C"
    elif score >= 60:
        print(f"Score: {score}\nGrade: D")
        grade = "D"
    else:
        print(f"Score: {score}\nGrade: F.")
        grade = "F"



def task5():
    # Name: Aurora Tackett
    # Date: 11/23/2026
    # Program: step03Tasks.py 
    # Description: drive?
    age = int(input("Age: "))
    perm = input("Do you have a permit? (y/n): ").strip().lower()
    lis = input("Do you have a lisense? (y/n): ").strip().lower()
    if age < 16:
        print("You cannot drive.")
    elif age < 16 and perm == "y" or lis == "y":
        print("You're either lying or stole a permit/lisense.")
    elif age >= 16:
        if perm == "y":
            print("You can drive with an adult.")
        elif perm == "n":
            print("Not yet.")
        elif lis == "y":
            print("You can drive on your own.")
        else:
            error()


def task6():
    # Name: Aurora Tackett
    # Date: 11/23/2026
    # Program: step03Tasks.py 
    # Description: poorly made rating system 
    rating = int(input("Rating (1-5): "))
    if rating >= 1 or rating <= 5:
        print(f"Thanks for the rating of {rating}")
    else:
        print("Rating must be between 1 and 5.") # I refuse to call this a true error. 


def task7():
    # Name: Aurora Tackett
    # Date: 11/23/2026
    # Program: step03Tasks.py 
    # Description: secret word! 
    word = "python"
    guess = input("Guess the word: ").strip().lower()
    if guess != word:
        print("Wrong guess.")
    elif guess == word:
        print("Correct!")
    else:
        error()


def task8():
    # Name: Aurora Tackett
    # Date: 11/23/2026
    # Program: step03Tasks.py 
    # Description: bigger number
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    if num1 > num2:
        print(f"{num1} is bigger.")
    elif num1 < num2:
        print(f"{num2} is bigger.")
    elif num1 == num2:
        print("They're equal.")
    else:
        error()


def task9():
    # Name: Aurora Tackett
    # Date: 11/23/2026
    # Program: step03Tasks.py 
    # Description: Free shipping and gift wrap. 
    order = float(input("Order total: "))
    wrap = input("Gift wrap? (y/n): ").lower()
    if order >= 50:
        shipping = 0
    else:
        shipping = 5.99
    if wrap == "y":
        wcost = 3
    else:
        wcost = 0
    total = wcost + shipping + order
    print(f"Final total: ${total}")


def task10():
    # Name: Aurora Tackett
    # Date: 11/23/2026
    # Program: step03Tasks.py 
    # Description: member price
    mem = input("Club member? (y/n): ").strip().lower()
    grade = int(input("Grade: "))
    if mem == "y":
        cost = 5
        if grade == 12:
            cost = 3
        elif grade != 12:
            pass
    elif mem == "n":
        cost = 8
    print(f"Your price: ${cost}")


def task11():
    # Name: Aurora Tackett
    # Date: 11/23/2026
    # Program: step03Tasks.py 
    # Description: Late fee
    FEE = 0.25
    late = int(input("Days late: "))
    if late == 0:
        fee = 0
    elif late > 0 or late < 20: 
        fee = FEE * late 
    elif late >= 20:
        fee = 5.00
    print(f"Late fee: ${fee:.2f}")


def main():
    while True:
        print("Which task would you like?")
        print("1. Problem 1")
        print("2. Problem 2")
        print("3. Problem 3")
        print("4. Problem 4")
        print("5. Problem 5")
        print("6. Problem 6")
        print("7. Problem 7")
        print("8. Problem 8")
        print("9. Problem 9")
        print("10. Problem 10")
        print("11. Problem 11")
        print("12. AM Hate Speech (optional)")
        print("Enter \"q\" to quit.")
        choice = input("Please type only the number: ")
        if choice == "1":
            task1()
            input()
            continue
        elif choice == "2":
            task2()
            input()
            continue
        elif choice == "3":
            task3()
            input()
            continue
        elif choice == "4":
            task4()
            input()
            continue
        elif choice == "5":
            task5()
            input()
            continue
        elif choice == "6":
            task6()
            input()
            continue
        elif choice == "7":
            task7()
            input()
            continue
        elif choice == "8":
            task8()
            input()
            continue
        elif choice == "9":
            task9()
            input()
            continue
        elif choice == "10":
            task10()
            input()
            continue
        elif choice == "11":
            task11()
            input()
            continue
        elif choice == "12":
            amHateSpeech()
            input()
            continue
        elif choice.lower() == "q":
            break
        else:
            print("Please type 1 for task A, 2 for task B, or 3 for task C.")
            continue


main()