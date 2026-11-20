def gpa():
    # Name: Aurora Tackett 
    # Date: 11/20/2026 
    # Project Name: gpaCheck.py
    # Description: Making a program to check GPA.

    gradeScale = {
        "A+": 4.0,
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,
        "C-": 1.7,
        "D+": 1.3,
        "D": 1.0,
        "D-": 0.7,
        "F": 0.0
    }
    #Starting numbers:
    totalQualityPoints = 0.0 
    totalCredits = 0.0 

    #Questions: 
    while True:
        try:
            classes = int(input("What's the number of classes you are calculating? "))
            if classes > 0:
                break
            print("Please enter at least 1 class.")
        except ValueError:
            print("Invalid input. Please put a whole number.")


    weight = input("Weighted GPA or Unweighted GPA? w/u ").strip().lower()


    def weightBonus():
        classtype = input("Is this a Regular, Honors, or AP/IB class? (r/h/ap/ib) ").strip().lower()
        if classtype == "h":
            return 0.5
        elif classtype in ("ap", "ib"):
            return 1.0
        else:
            return 0.0

    print("In college, credits span from 1-5, and High School is from 1.0 for a full year class, " \
        "and 0.5 for a semester long.")

    #Loop: 
    for i in range(classes):
        print(f"\n--- Class {i + 1} ---")

        #Validate Credits:
        while True:
            try:
                credits = float(input("How many credits/units is this class worth? "))
                if credits > 0:
                    break
                print("Credits must be greater than 0")
            except ValueError:
                print("Invalif input. Please enter a number (like 1.0 or 0.5).")

        while True:
            grade = input("What is your grade in the class? ").upper()
            if grade in gradeScale:
                break
            print("Invalid grade. Please enter a valid letter grade (A+ through F).")

        # Dictionary check
        grade = gradeScale[grade.upper()]

        if weight.lower() == "w" and grade > 0:
            grade += weightBonus()

        QualityPoints = grade * credits
        totalQualityPoints += QualityPoints
        totalCredits += credits

    gpa = totalQualityPoints / totalCredits
    print(f"\nYour final GPA is: {round(gpa, 2)}")

gpa()