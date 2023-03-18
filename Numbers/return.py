# Change Return Program
# The user enters a cost and then the amount of money given.
# The program will figure out the change and the number of quarters,
# dimes, nickels, pennies needed for the change.

coins = {'Quarter': 0.25, 'Dime': 0.1, 'Nickel': 0.05, 'Pennie': 0.01}

cost = float(input('Enter cost: '))
money_given = float(input('How much money given: '))

rest = money_given - cost

for coin in coins:
    print(f'{coin}: {int(rest // coins[coin])}')
    rest = round(rest % coins[coin], 2)
    if not rest:
        break
