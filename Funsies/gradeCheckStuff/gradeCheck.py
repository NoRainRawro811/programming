def testGradeCheck():
    # Name: Aurora Tackett 
    # Date: 11/19/2026 
    # Project Name: gradeCheck.py 
    # Description: A program to check my grades. 

    print("Please enter only numbers.")

    # Inputs: 
    score = int(input("What did you get? "))
    outOf = int(input("What was it out of? "))

    # Functions to save time: 
    def conLetGrade():
        print(f"You got a {numberGrade:.2f}%.\nThat's a {letterGrade}.")
    def vowLetGrade():
        print(f"You got a {numberGrade:.2f}%.\nThat's an {letterGrade}.")

    # Math: 
    numberGrade = score / outOf * 100 

    # If statement section! 
    if numberGrade >= 97:
        letterGrade = "A+" 
        gpa = 4.0
        vowLetGrade()
    elif numberGrade >= 93:
        letterGrade = "A"
        gpa = 4.0 
        vowLetGrade()
    elif numberGrade >= 90:
        letterGrade = "A-"
        gpa = 3.7
        vowLetGrade()
    elif numberGrade >= 87:
        letterGrade = "B+"
        gpa = 3.3
        conLetGrade()
    elif numberGrade >= 83:
        letterGrade = "B"
        gpa = 3.0
        conLetGrade()
    elif numberGrade >= 80:
        letterGrade = "B-"
        gpa = 2.7
        conLetGrade()
    elif numberGrade >= 77:
        letterGrade = "C+"
        gpa = 2.3
        conLetGrade()
    elif numberGrade >= 73:
        letterGrade = "C"
        gpa = 2.0
        conLetGrade()
    elif numberGrade >= 70:
        letterGrade = "C-"
        gpa = 1.7 
        conLetGrade()
    elif numberGrade >= 67:
        letterGrade = "D+"
        gpa = 1.3
        conLetGrade()
    elif numberGrade >= 63:
        letterGrade = "D"
        gpa = 1.0 
        conLetGrade()
    elif numberGrade >= 60:
        letterGrade = "D-"
        gpa = 0.7
        conLetGrade()
    elif numberGrade < 60:
        letterGrade = "F"
        gpa = 0.0
        vowLetGrade()

testGradeCheck()

