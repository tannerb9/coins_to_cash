

def calc_dollars(**coins):
    dollar_amount = []
    for key, value in coins.items():
        if key == "pennies":
            dollar_amount.append(value * .01)
        elif key == "nickels":
            dollar_amount.append(value * .05)
        elif key == "dimes":
            dollar_amount.append(value * .1)
        elif key == "quarters":
            dollar_amount.append(value * .25)

    dollar_amount = dollar_amount[0] + dollar_amount[1] + \
        dollar_amount[2] + dollar_amount[3]

    print(dollar_amount)


calc_dollars(pennies=342, nickels=9, dimes=32, quarters=4)
