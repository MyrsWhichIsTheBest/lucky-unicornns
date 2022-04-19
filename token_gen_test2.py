import random
import math

tokens = {
    "donkey": 1,
    "horse": 2,
    "zebra": 3,
    "unicorn": 4
}


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return int(math.floor(n * multiplier) / multiplier)


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
        gemfinal = balance - original_ammount
        gems_gained = balance
        gems_change = gemfinal + balance
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
    return gems_change


# main
while True:
    while True:
        gemraw = input("How much would you like to spend? $")
        try:
            int(gemraw) + 1
        except:
            print("Error!")
        else:
            gemraw = int(gemraw)
            if gemraw <= 0:
                print("Invalid Input!")
            else:
                break
    wish_funct(gemraw)
    choice = input("Would you like to wish again?")
