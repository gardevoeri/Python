import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 'heads' or 'tails' values.
    coin = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            coin.append("H")
        else:
            coin.append("T")

    # Code that checks if is a streak of 6 heads or tails in a row.
    count = 0
    for j in range(len(coin) - 1):
        if coin[j] == coin[j + 1]:
            count += 1
        else:
            count = 0
        if count == 6:
            numberOfStreaks += 1
            count = 0

print("Chance of streak: %s%%" % (numberOfStreaks / 100))
