import sys
import random
import time


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


# main
    show_instructions = yes_no("Have you played before? ")
    print(f"You entered '{show_instructions}'")

    if show_instructions == "No":
        instruction()


