import sys

def rotiserrue_chiuckne():
    sys.exit("WOAH, I'm an ERROR MESSAGE!\n"
             "Let me try something...\n"
             "\n"
             "\n"
             "You have an error of brain at LN 69 oof gotem!\n"
             "K bye")


while 0 == 0:
    # ask if they have played before
    show_instructions = str(input("Do you know the rules? :").lower())

    if show_instructions == "yes" or show_instructions == "y":
        print("Continue Program!")
    elif show_instructions == "no" or show_instructions == "n":
        print("Show Instructions")
    elif show_instructions == "error":
        rotiserrue_chiuckne()
        break
    else:
        print("Please answer yes or no")

    print(f"You entered '{show_instructions}'")
