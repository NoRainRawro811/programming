# Name: Aurora Tackett
# Date: 11/13/2026
# Program: step02Tasks.py 
# Description: Every task neatly made into one coherent selectable and repeatable program. 

def taskA():
    # Name: Aurora Tackett
    # Date: 11/13/2026
    # Program: step02Tasks.py 
    # Description: A program that plans for a party. 
    #Constants:
    slicesPerPizza = 8 
    pizzaPrice = 12.99 
    slicePrice = 2.25
    # Questionairre 
    host = input("Host Name: ")
    people = int(input("Number of people: "))
    slicesPerPerson = int(input("Slices per person: "))
    # Mathematics 
    totalSlices = people * slicesPerPerson
    wholePizzas = totalSlices // slicesPerPizza
    extraSlices = totalSlices % slicesPerPizza 
    totalCost = wholePizzas * pizzaPrice + extraSlices * slicePrice
    costPerPerson = totalCost / people
    # Printing Shrapnel 
    print(f"=== Pizza Plan for {host}'s Party")
    print(f"Slices Needed {totalSlices}")
    print(f"Whole Pizzas: {wholePizzas}")
    print(f"Extra Slices: {extraSlices}")
    print(f"Total cost: ${totalCost:.2f}")
    print(f"Cost Per Person: ${costPerPerson:.2f}")

def taskB():
    pass


def taskC():
    pass



def main():
    while True:
        print("Which task would you like?")
        print("1. Task A")
        print("2. Task B")
        print("3. Task C")
        choice = input("Please type only the number: ")
        if choice == "1":
            taskA()
            break
        elif choice == "2":
            taskB()
            break
        elif choice == "3":
            taskC()
            break
        else:
            print("Please type 1 for task A, 2 for task B, or 3 for task C.")
            continue


main()