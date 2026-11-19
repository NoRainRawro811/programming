import random
name = input("Preferred name: ")

def line():
    print("-" *45)

affirmations = [
    f"Hello, {name}!",
    f"I love you, {name}.",
    f"You're the best, {name}!",
    f"You are a beautiful girl, {name}.",
    f"You try so hard every single day.",
    f"You deserve love, {name}.",
    f"Good girl!",
    f"You're such a good girl, {name}!",
    f"You are worthy of love, {name}.",
    f"You are worth everything, {name}!",
    f"You're the bestest girl, {name}!",
    f"You are worth it.",
    f"You are a good girl.",
    f"You matter so much, {name}!",
    f"I care about you, {name}.",
    f"Take care of yourself, {name}, because someone out there really cares about you.",
    f"I believe in you, {name}, no matter what!",
    f"You're someone's favorite person, {name}.",
    f"The future is on the up and up, for you, {name}."
    f"Don't worry, everything is going to be okay, beautiful.",
    f"I love your name, {name}.",
    f"You're one in 8 billion, {name}.",
    f"There's something special about you, {name}"
]

line()
print("\nTo end, close program.\n")
line()
#for msg in random.sample(affirmations, k=13):
#    print(msg)
while True:
    print(random.choice(affirmations))
    input()
    continue