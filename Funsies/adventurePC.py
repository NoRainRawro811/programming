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
        elif choice == "":
            break
        else:
            print("Type Y for Yes or N for No.")
    print("CONTROLS:")
    print("Type the selection keys for your choices\nBetween text, you must press 'enter' to progress.")
    print("Now, press 'enter' to begin.")
    choice = input()
    if choice == "":
        pass
    elif choice == "dev":
        devMenu()
    else:
        print("Press enter.")

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
            continue
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
        print("1. Approach the light")
        print("2. Run from the light")
        print("3. Stand your ground")
        choice = input("Action: ")
        if choice == "1":
            playerChoices.append("Nightmare_Approached")
            personality["curiosity"] =+ 2
            personality["bravery"] =+ 1
            print("You approach the light...")
            input()
            print("You reach out your hand...")
            input()
            print("You hear something rustling...")
            input()
            print("The light grows brighter until...")
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
            continue

def getReadyM():
    pass

def getReadyF():
    pass


def wakeConvoM():
    if "Nightmare_Approached" in playerChoices:
        print("You open your eyes to see your friend and roommate stumbling to put his boots on.")
        input()
        while True:
            print("What to do...")
            print("1. Get up")
            print("2. Stay in bed because fuck you")
            print("3. Talk to your roommate")
            choiceA = input("Type the number: ")
            if choiceA == "1":
                print("You decide to get up, dragging yourself out of bed.")
                input()
                break
            elif choiceA == "2":
                print("Yeah, screw this. You stay in bed.")
                input()
                print("\"" + playerName + ", get out of bed. We're gonna be late as is.\"")
                input()
    
    elif "Nightmare_Ran" in playerChoices:
        print("You wake up to see your friend/roommate right in your face.")
        input()
        print("\"Dude, wake up, we're gonna be SO late!\"")
        input()
    
    elif "Nightmare_Stood" in playerChoices:
        print("""Dude, wake the hell up, we're gonna be late!""")
        input()
        print("You open your eyes to see your friend and roommate shaking you awake.")
        input()


def wakeConvoF():
    if "Nightmare_Approached" in playerChoices:
        print("You open your eyes to see your friend and roommate stumbling to put her boots on.")
        input()
        while True:
            print("What are you gonna do?")
            print("1. Get up")
            print("2. Stay in bed")
            print("3. Talk to roomie")
            choiceA = input("Type the number: ")
            if choiceA == "1":
                print("Yeah, you probably should...")
                input()
                print("You drag yourself out of bed.")
                input()
                getReadyF()
                break
            elif choiceA == "2":
                print("You snuggle up in the covers. You're pretty comfortable anyway.")
                input()
                print("You close your eyes, but your comfiness ends abruptly as your blanket gets torn away from you!")
                input()
                print("\"Oh my gods, wake up and STAY UP, " + playerName + "!\"")
                input()
                print("Well, I suppose you don't have much of a choice now.")
                input()
                print("You choose to get up.")
                input()
                getReadyF()
                break
            elif choiceA == "3":
                print("You stir and sit upwards.")
                input()
                print("But before you can get a word out, your roommate goes over to you.")
                input()
                print("\"Oh my gods, get dressed, we're gonna be late to class.\"")
                input()
                print("Reluctantly, you get ready.")
                input()
                getReadyF()
                break
            else:
                print("Please choose a choice out of the selection.")
                continue


    elif "Nightmare_Ran" in playerChoices:
        print("You wake up to the concerned face of your roommate.")
        input()
        print("""You were squirming in your sleep, are you alright...?""")
        input()
        print("""Oh, right, um, we're gonna be late REALLY soon!""")
        input()

    elif "Nightmare_Stood" in playerChoices:
        print("""Wake up, for the love of the gods, we're gonna be late!""")
        input()
        print("You wake up to the sight of your friend and roommate giving you a bit of a glare.")
        input()
        print("On second thought, they look more or less stressed.")



def wake01():
    if "Nightmare_Approached" in playerChoices:
        if playerGender == "M":
            wakeConvoM()
        elif playerGender == "F":
            wakeConvoF()
    elif "Nightmare_Ran" in playerChoices:
        if playerGender == "M":
            wakeConvoM()
        elif playerGender == "F":
            wakeConvoF()
    elif "Nightmare_Stood" in playerChoices:
        if playerGender == "M":
            wakeConvoM()
        elif playerGender == "F":
            wakeConvoF()




def main():
    intro()
    name()
    gender()
    nightmare()
    wake01()




def devMenu():
    line()
    print("This is the dev menu.")
    line()
    print("A bit broken.")
    playerGender = "F"
    playerName = "Queen"
    playerChoices.append("Nightmare_Approached")
    while True:
        print("Choose between the following:")
        print("intro\nname\ngender\nnightmare\nwake01")
        choice = input("Choose a scene: ")
        if choice == "intro":
            intro()
        elif choice == "name":
            name()
        elif choice == "gender":
            gender()
        elif choice == "nightmare":
            nightmare()
        elif choice == "wake01":
            wake01()
        else:
            print("Not a choice.")



main()