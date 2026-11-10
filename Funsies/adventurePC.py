def line():
    print("-" * 50)

playerChoices = []

personality = {
    "curiosity": 0, # Interest in the unknown 
    "bravery": 0, # Willingness to face danger 
    "defiance": 0, # Resistance to authority 
    "caution": 0, # Preference for safety 
    "compassion": 0, # Willingness to help others 
    "cruelty": 0, # Selfishness or malicious intent 
    "certainty": 0 # Confidence in one's decisions 
}

def intro():
    line()
    print("Welcome to Adventure PC!")
    line()
    while True:
        print("Would you like to know more about APC?")
        choice = input("Y/N: ")
        if choice == "Y":
            print("Adventure originated as a program I was coding for my TI-84 Python calculator.")
            print("And I decided to try porting it to PC when I have time in my Software Engineering class.")
        elif choice == "N":
            break
        else:
            print("Type Y for Yes or N for No.")
    print("CONTROLS:")
    print("Type the selection keys for your choices\nBetween text, you must press 'enter' to progress.")
    print("Now, press 'enter' to begin.")
    input()

def gender():
    global playerGender
    print("Now, please select your preferred gender.")
    while True:
        print("1. Male")
        print("2. Female")
        choice = input("Please select a gender. ")
        if choice == "1":
            playerGender = "M"
            break
        elif choice == "2":
            playerGender = "F"
            break
        else:
            print("Please select one of the given choices.")
    if playerGender == "M":
        print("Alright then, " + playerName + ", let's begin.")
        input()
    elif playerGender == "F":
        print("Thank you, " + playerName + ", we will begin now.")
        input()

def name():
    global playerName
    print("Before we begin, what is your name?")
    print("Note: this cannot be changed later.")
    playerName = input("Please put your name: ")
    while True:
        print("Would you like to change your name?")
        choice = input("Y/N: ")
        if choice == "Y":
            name()
        elif choice == "N":
            break
        else:
            print("Please select Y for Yes and N for No.")
    print(playerName)

def test():
    if playerGender == "M":
        print("Boy")
    elif playerGender == "F":
        print("Girl")
    elif playerGender == "N":
        print("Human.")
    print(playerName)
    print(playerGender)

def nightmare():
    line()
    print("Chapter 1: First Steps")
    line()
    print("It's dark, and you can't see anything ahead of you.")
    input()
    print("No... Wait, you see a light.")
    input()
    print("But what will you do?")
    while True:
        choice = input("Action: ")
        print("1. Approach the light")
        print("2. Run from the light")
        print("3. Stand your ground")
        if choice == "1":
            playerChoices.append("Nightmare_Approached")
            personality["curiosity"] =+ 2
            personality["bravery"] =+ 1
            print("You approach the light...")
            input()
            print("You reach out your hand...")
            input()
            break
        elif choice == "2":
            playerChoices.append("Nightmare_Ran")
            personality["caution"] =+ 1
            print("Aw, hell no. You run away from that!")
            input()
            print("But as you run into the abyss, you hear a voice...")
            input()
            print("It's familiar...")
            input()
            break
        elif choice == "3":
            playerChoices.append("Nightmare_Stood")
            personality["defiance"] =+ 1
            personality["certainty"] =+ 2
            print("You stand your ground, looking that light right up.")
            input()
            print("But you hear something...")
            input()
            print("Or is it... Some ONE?")
            input()
            break
        else:
            pass

def wake01():
    if "Nightmare_Approached" in playerChoices:
        if playerGender == "M":
            print("You open your eyes to see your friend and roommate stumbling to put his boots on.")
        elif playerGender == "F":
            print("You open your eyes to see your friend and roommate stumbling to put her boots on.")
    elif "Nightmare_Ran" in playerChoices:
        if playerGender == "M":
            print("You wake up to see your friend/roommate right in your face.")
            input()
            print("""Dude, wake up, we're gonna be SO late!""")
        elif playerGender == "F":
            print("You wake up to the concerned face of your roommate.")
            input()
            print("""You were squirming in your sleep, are you alright...?""")
            input()
            print("""Oh, right, um, we're gonna be late REALLY soon!""")
    elif "Nightmare_Stood" in playerChoices:
        if playerGender == "M":
            print("""Dude, wake the hell up, we're gonna be late!""")
            print("You open your eyes to see your friend and roommate shaking you awake.")
        elif playerGender == "F":
            print("""Wake up, for the love of the gods, we're gonna be late!""")
            print("You wake up to the sight of your friend and roommate giving you a bit of a glare.")




def main():
    intro()
    name()
    gender()
    nightmare()
    wake01()








main()