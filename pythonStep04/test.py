for i in range(4):
    print("I'm taking a step.")


# Backspace 1

for number in range(2, 12, 3):
    print(number)

# Backspace 2

for number in range(1, 6):
    print(number, end=", ")


# Backspace 3 

for number in range(1, 6):
    print(f"{number} doubled is {number * 2}")


# Backspace 4

name = input("Your name: ")
times = int(input("How many times do you want your name printed? "))

for i in range(times):
    print(name)


# backspace 5

for step in range(1, 11):
    print("#" * step)


# Backspace 6

total = 0

for number in range(1, 6):
    total = total + number
    print(f"Added {number}, total is now {total}")

print(f"Final total is {total}")

# Backspace 7

count = 1

while count <= 5:
    print(count)
    count = count + 1

print("\u2588Done\u2591")

SECRET = "tikibaha"
guess = input("Guess the secret word: ")

while guess != SECRET:
    print("Nope. Try again.")
    guess = input("Guess the secret word: ")
    if guess == "e":
        break

print("You got it!")

# Backspace 8

#Asking if ywanna keep playing
answer = "yes"
rounds = 0

while answer == "yes" or "y":
    rounds = rounds + 1 
    print(f"Playing round {rounds}")
    answer = input("yes or no: ").lower().strip()
    if answer == "no" or "n":
        break


print(f"You got to round {rounds}. Thx for 'playing'.")
