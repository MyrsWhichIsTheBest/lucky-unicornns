import sys
import random
import time
import math


def rotiserrue_chiuckne(bhr):
    sys.exit(f"WOAH, I'm an ERROR MESSAGE!\n"
             f"Let me try something...\n"
             f"\n"
             f"\n"
             f"You have an error of {bhr} at LN 69 oof gotem!\n"
             f"K bye")


def yes_no(question_text):
    while True:
        # ask if they have played before
        answer = input(question_text).lower()

        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer
        elif answer[-1] == "?":
            rotiserrue_chiuckne(answer)
        else:
            print("Please answer yes or no")


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return int(math.floor(n * multiplier) / multiplier)


def instruction():
    time.sleep(1)
    print("**** How to Play ****\n"
          "\n"
          "Your money will be converted to Gems.\n"
          "Each Roll costs 160 Gems (around a dollar).\n"
          "The outcome can be one of 4 animals.\n"
          "Donkey - You gain nothing back.\n"
          "Horse - You gain half of your gems back.\n"
          "Zebra - You gain all of your gems back plus 20 more.\n"
          "Unicorn - You gain all of your gems back plus 1600 more!\n"
          "\n"
          "Cont.\n")
    time.sleep(0.6)


def wish_funct(balance):
    while True:
        while True:
            hmr = balance % 160
            print(f"You will be able to roll {hmr} times.")
            while True:
                amount = input("How much would you like to roll?")
                try:
                    int(amount) + 1
                except:
                    print("Error!")
                else:
                    amount = int(amount)
                    if amount <= 0:
                        print("Invalid Input!")
                    else:
                        original_ammount = balance
                        break
            if amount <= hmr:
                break
            else:
                print("Amount is more than current balance!")
        print("Rolling...")
        time.sleep(1.3)
        for i in range(hmr):
            roll = random.randint(1, 30)
            if roll <= 15:
                print("Donkey!")
                balance = balance - 160
            elif roll <= 25:
                print("Horse!")
                balance = balance - 80
            elif roll <= 29:
                print("Zebra!")
                balance = balance + 20
            else:
                print("Unicorn!")
                balance = balance + 1600
            time.sleep(0.2)
        gems_gained = balance
        dollars = round_down(gems_gained / 160 + original_ammount)
        final_amount = original_ammount - dollars
        if final_amount < 0:
            final_amount *= -1
        if dollars == original_ammount:
            print("You broke even!")
        elif dollars < original_ammount:
            print(f"You lost ${final_amount}")
        else:
            print(f"You gained ${final_amount}!")
        break
    return balance


# main
show_instructions = yes_no("Have you played before? ")
print(f"You entered '{show_instructions}'")
if show_instructions == "No":
    instruction()
while True:
    while True:
        gemraw = input("How much would you like to spend? $")
        try:
            int(gemraw) + 1
        except:
            print("Invalid Input!")
        else:
            gemraw = int(gemraw)
            if gemraw <= 0:
                print("Invalid Input!")
            else:
                break
    wish_funct(gemraw)
    choice = yes_no("Do you want to play again?")
    if choice == "No":
        break
