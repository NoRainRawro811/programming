from time import sleep as wait
import random
from random import randint, uniform

def mycode():
    for i in range(5):
        print(f"\rLoading... {i * 25}%", end="", flush=True)
        wait(.5)

    print("\rDone!                  ")

def gemcode():
    total_steps = 20

    for i in range(total_steps + 1):
      percent = i * 5
      filled = "#" * i
      empty = "-" * (total_steps - i)

      print(f"\rLoading: [{filled}{empty}] {percent}%", end="", flush=True)
      wait(0.15)

    print("\rDone!                                  ")


def gemrand():
    progress = 0
    bar_length = 20

    while progress < 100:
      # Jump forward by a random amount between 1% and 12%
      progress += random.randint(1, 12)
      if progress > 100:
        progress = 100  # Cap it so it doesn't go over 100%

      # Calculate how many '#' symbols match the current percentage
      filled_count = int((progress / 100) * bar_length)
      filled = "█" * filled_count
      empty = "░" * (bar_length - filled_count)

      print(f"\rLoading: [{filled}{empty}] {progress}%", end="", flush=True)

      # Pause for a random time between 0.05 and 0.6 seconds
      wait(random.uniform(0.05, 0.6))

    print("\rDone!                                      ")


def myrand():
    progress = 0
    barLength = 20
    filledCount = int((progress / 100) * barLength)
    filled = "\u2588" * barLength # makes █
    empty = "\u2591" * (barLength - filledCount) # makes ░
    while progress < 100:
       progress += randint(1, 12)
       if progress > 100:
          progress = 100
       filledCount = int((progress / 100) * barLength)
       filled = "█" * filledCount
       empty = "░" * (barLength - filledCount)
       print(f"\rLoading: [{filled}{empty}] {progress}%", end="", flush=True)
       wait(uniform(0.05, 0.6))
    print("\nLoading: Done!")



def main():
    while True:
        choice = input("mycode, gemcode, gemrand, myrand? ").strip().lower()
        if choice == "mycode":
            mycode()
            continue
        elif choice == "gemcode":
            gemcode()
            continue
        elif choice == "gemrand":
           gemrand()
           continue
        elif choice == "q":
           break
        elif choice == "myrand":
           myrand()
        else:
           continue

main()