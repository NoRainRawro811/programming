from Funsies.functioning.funniFunctionsToNeverCall import amHateSpeech

amHateSpeech()

player = "Avery"
points = 42 

print(f"{player} scored an average of {points} points.")

# Backspaced. 

quantity = int(input("How many? "))
price = float(input("Price each: "))
print(f"Total amount: {quantity * price}")

# Backspace 2. 

slices = 40 

wholePizza = slices // 8 
extraSlices = slices % 8
print(f"We need {wholePizza} pizzas.")
print(f"We need {extraSlices} slices.")

# Backspace 3. 

total = 7.5
print(f"Total ${total:.2f}")

# Backspace 4. 
ticketPrice = 8.50
taxRate = 0.07

tickets = int(input("Tickets: "))
subtotal = ticketPrice * tickets 
tax = subtotal * taxRate 
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}") 
print(f"Total: ${subtotal + tax:.2f}")