from Funsies.gradeCheckStuff.gradeCheck import testGradeCheck



def main():
    while True:
        print("Which would you like to check?")
        print("1. A current test grade")
        print("2. Your GPA")
        print("3. TBA")
        choice = input("Put the number: ")
        if choice == "1":
            testGradeCheck()




main()

