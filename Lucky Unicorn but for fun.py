import sys
import random
import time


user_gems = 0


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


def instruction():
    time.sleep(1)
    print("**** How to Play ****\n"
          "\n"
          "The rules\n"
          "\n"
          "Cont.\n")
    time.sleep(0.6)


def credit_recharge():
    error = "Please enter an int (Whole Number) greater or equal to 1!\n"
    valid = False
    global user_gems

    while not valid:
        try:
            # ask amma
            user_balance = int(input("How much would you like to use?"))

            # check if the amma is too high or too low
            if 0 < user_balance:
                if user_balance >= 10:
                    print(f"Are you sure that you want to use ${int(user_balance)}?")
                    choice = input().lower()[1]
                    if choice == "n":
                        credit_recharge()
                    elif choice == "y":
                        bonus_gems = user_balance % 3.5 * 100
                        user_balance *= 175 + bonus_gems
                        user_gems = round(user_balance)
                        print(f"You have {user_gems} gems!")
                        valid = True
            else:
                print(error)

        except ValueError:
            print(error)


# main
show_instructions = yes_no("Have you played before? ")
print(f"You entered '{show_instructions}'")

if show_instructions == "No":
    instruction()
print("Starting game up...")
time.sleep(1.8)
credit_recharge()
print("1 Wish costs 200 gems. A 10 Wish costs 2000 gems.")
wishes_possible = user_gems % 200
print(f"You can do {wishes_possible}.")

