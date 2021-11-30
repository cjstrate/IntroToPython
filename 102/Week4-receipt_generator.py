# Carter Strate
# CSCI 102 - Section D
# Week 4 - Lab A - Receipt Generator
# References: Assignment for formatting
# Time: 30 minutes

nameC = input('Enter company name: ')
cityC = input('Enter company city/state: ')
# pi = priced item (N = name) (P = price)
nameCA = input('Enter cashier name: ')
pi1N = input('Purchased item 1 name: ')
pi1P = float(input('Purchased item 1 price: '))
pi2N = input('Purchased item 2 name: ')
pi2P = float(input('Purchased item 2 price: '))
pi3N = input('Purchased item 3 name: ')
pi3P = float(input('Purchaed item 3 price: '))
# Favorite ending message
fem = input('Enter your favorite ending message: ')

total = pi1P + pi2P + pi3P
# Spacing is weird depending of input length
print(f'''\n            RECEIPT GENERATOR
    -----------------------------------
        {nameC}
        {cityC}
    ===================================
        Your cashier was: {nameCA}
        Welcome Valued Customer
    ===================================
        Item Name       Item Price

        {pi1N} ${pi1P:.2f}
        {pi2N}          ${pi2P:.2f}
        {pi3N}     ${pi3P:.2f}

    ===================================
        Total Cost of Order: {total:.2f}
    ===================================
        {fem}
    -----------------------------------''')
