
def credit_recharge():
    error = "Please enter an int (Whole Number) greater or equal to 1!\n"
    valid = False

    while not valid:
        try:
            # ask amma
            user_balance = int(input("How much would you like to use?"))

            # check if the amma is too high or too low
            if 0 < user_balance:
                if user_balance >= 10:
                    print(f"Are you sure that you want to use ${user_balance}?")
                    if input().lower()[1] == "n":
                        credit_recharge()
                bonus_gems = user_balance % 3.5 * 100
                user_balance *= 175 + bonus_gems
                user_gems = round(user_balance)
                print(f"You have {user_gems} gems!")
                valid = True
            else:
                print(error)

        except ValueError:
            print(error)


while True:
    credit_recharge()
