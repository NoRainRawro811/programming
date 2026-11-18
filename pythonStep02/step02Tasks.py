from Funsies.functioning.funniFunctionsToNeverCall import amHateSpeech
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
    # Name: Aurora Tackett
    # Date: 11/13/2026
    # Program: step02Tasks.py 
    # Description: Something about travel 
    destination = input("Where you headed? ") 
    tripDistance = float(input("What was your trip distance in miles? "))
    milesPerGallon = float(input("What's your Miles Per Gallon? "))
    gasPrice = float(input("What's the gas price? "))
    peopleSplit = int(input("How many people are splitting the cost?"))
    averageSpeed = 55
    gallons = tripDistance / milesPerGallon 
    gasCost = gallons * gasPrice 
    costPerPerson = gasCost / peopleSplit 
    minutes = tripDistance / averageSpeed * 60 # make an int
    hours = minutes // 60 
    leftoverMinutes = minutes % 60
    roundTrip = gasCost * 2
    print(f"Destination: {destination}")
    print(f"Trip distance (miles): {tripDistance}")
    print(f"Car's miles per gallon: {milesPerGallon}")
    print(f"Gas price per gallon: {gasPrice}")
    print(f"Number of people splitting the cost: {peopleSplit}")
    print(f"\n--- Trip to {destination} ---")
    print(f"Gallons of gas:     {gallons:.1f}")
    print(f"Gas cost:           {gasCost:.2f}")
    print(f"Cost per person:    {costPerPerson:.2f}")
    print(f"Driving time:       {hours} hr {minutes} min (at {averageSpeed} mph)")
    print(f"Round trip cost:    {roundTrip:.2f}")


def taskC():
    # Name: Aurora Tackett
    # Date: 11/13/2026
    # Program: step02Tasks.py 
    # Description: Something about paychecks. 
    name = input("Name: ")
    hourlyPayRate = float(input("Hourly pay rate: "))
    hours = float(input("Hours worked this week: "))
    federalTaxRate = 0.10
    stateTaxRate = 0.035 
    socialSecurityRate = 0.062
    medicareRate = 0.0145 
    weeksPerYear = 52
    totalOut = medicareRate + stateTaxRate + federalTaxRate + socialSecurityRate
    grossPay = hourlyPayRate * hours
    eachTax = hourlyPayRate * totalOut
    netPay = hourlyPayRate - totalOut
    percentKept = netPay / grossPay * 100
    yearlyGross = grossPay * weeksPerYear 
    yearlyNet = netPay * weeksPerYear
    print("=" * 32)
    print(f"PAY STUB: {name}")
    print("=" * 32)
    print(f"Hours worked:        {hours:.1f}")
    print(f"Hourly Rate          ${hourlyPayRate:.2f}")
    print(f"Gross Pay            ${grossPay:.2f}")
    print("-" * 32)
    print(f"Federal tax (10%):   ${federalTaxRate:.2f}")
    print(f"State tax (3.5%):    ${stateTaxRate:.2f}")
    print(f"Social Security:     ${socialSecurityRate:.2f}")
    print(f"Medicare:            ${medicareRate:.2f}")
    print(f"Total taken out:     ${totalOut:.2f}")
    print("-" * 32)
    print(f"NEXT PAY:            ${grossPay}")
    print("=" * 32)
    print(f"You keep 78.8% of what you earn")
    print(f"Yearly gross:        ${yearlyGross:.2f}")
    print(f"Yearly net:          ${yearlyNet:.2f}")



def main():
    while True:
        print("Which task would you like?")
        print("1. Task A")
        print("2. Task B")
        print("3. Task C")
        print("4. AM Hate Speech (optional)")
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
        elif choice == "4":
            amHateSpeech()
            break
        else:
            print("Please type 1 for task A, 2 for task B, or 3 for task C.")
            continue


main()