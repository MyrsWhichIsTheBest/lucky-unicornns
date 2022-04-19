import random

tokens = {
    "donkey": 1,
    "horse": 2,
    "zebra": 3,
    "unicorn": 4
}
while 0 == 0:
    balance = input("INT in $")
    try:
        int(balance) + 1
    except:
        print("Error!")
    else:
        break

starting = balance
balance *= 160
pity = 0
hmr = 1000

#while balance >= 160:
#while hmr >= 0:
for i in range(10):
    roll = random.randint(1, 30)
    if pity < 5:
        if roll <= 7:
            print("Donkey!")
            balance -= 160
            pity += 1
        elif roll <= 19:
            print("Horse!")
            balance -= 80
            pity += 1
        elif roll <= 27:
            print("Zebra!")
            balance += 20
            pity += 1
        else:
            print("Unicorn!")
            balance += 1000
            pity = 0
    elif pity < 15:
        if roll <= 20:
            print("Donkey!")
            balance -= 160
            pity += 1
        elif roll <= 25:
            print("Horse!")
            balance -= 80
            pity += 1
        elif roll <= 29:
            print("Zebra!")
            balance += 20
            pity += 1
        else:
            print("Unicorn!")
            balance += 1000
            pity = 0
    elif pity < 30:
        if roll <= 10:
            print("Donkey!")
            balance -= 160
            pity += 1
        elif roll <= 20:
            print("Horse!")
            balance -= 80
            pity += 1
        elif roll <= 29:
            print("Zebra!")
            balance += 20
            pity += 1
        else:
            print("Unicorn!")
            balance += 1000
            pity = 0
    else:
        if roll <= 5:
            print("Donkey!")
            balance -= 160
            pity += 1
        elif roll <= 15:
            print("Horse!")
            balance -= 80
            pity += 1
        elif roll <= 20:
            print("Zebra!")
            balance += 20
            pity += 1
        else:
            print("Unicorn!")
            balance += 800
            pity = 0
    hmr =+ 1


print(f"{balance} gems left!")
print(f"{hmr} runs")
fb = balance/160
ffb = fb - starting
print(f"Your final balance is... ${fb}\n"
      f"You gained ${ffb}!")
