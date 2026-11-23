from Funsies.gradeCheckStuff.gradeCheck import testGradeCheck
from Funsies.gradeCheckStuff.gpaCheck import gpa


def main():
    while True:
        print("Which would you like to check?")
        print("1. A current test grade")
        print("2. Your GPA")
        print("3. TBA")
        choice = input("Put the number: ")
        if choice == "1":
            testGradeCheck()
            break
        elif choice == "2":
            gpa()
            break




main()