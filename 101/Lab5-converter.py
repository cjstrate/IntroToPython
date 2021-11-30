# Carter Strate
# CSCI 101 - Section G
# Python Lab 5
# References: none
# Time: 60 minutes

print('Welcome to the Binary-Decimal Converter\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
x = 1
while x == 1:
    print('Enter an option:\n1. Binary-Decimal Conversion\n2. Decimal-Binary Conversion\n3. Quit')
    oper = int(input('OPTION> '))

    if oper == 1:
        l = []
        decimal = 0
        binary = input('BINARY_STR> ')
        for elem in binary:
            l.append(elem)
        for pe in l:
            if pe == '1':
                continue
            elif pe == '0':
                continue
            else:
                print(f'ERROR: Input {pe} is NOT a binary number.')
                x = 2
        if x == 2:
            break
        l.reverse()
        index = 0
        for value in l:
            if int(value) == 0:
                index += 1
            elif int(value) == 1:
                decimal = decimal + 2**index
                index += 1
        print(f'Binary {binary} is Decimal {decimal}\nOUTPUT {decimal}')

    elif oper == 2:
        l = []
        value = None
        string = ''
        decimal = input('DECIMAL-STR> ')
        try:
            decimal = int(decimal)
        except:
            x ==2
            print(f'ERROR: Input {decimal} is NOT a decimal number.')
            break
        decimal2 = decimal
        while value != 0:
            remainder = int(decimal % 2)
            decimal = decimal // 2
            string = string + str(remainder)
            value = decimal
        for elem in string:
            l.append(elem)
        l.reverse()
        string = ''
        for x in l:
            string = string + x
        print(f'Decimal {decimal2} is Binary {string}\nOUTPUT {string}')
    elif oper == 3:
        x = 2
        continue

    else:
        print('ERROR: Please choose from [1-3]')

    cont = input('Would you like to continue (y/n)?\nCONTINUE> ')
    y = 1
    while y == 1: 
        if cont[0] == 'Y':
            y = 2
            print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        elif cont[0] == 'y':
            y = 2
            print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        elif cont[0] == 'N':
            y = 2
            x = 2
        elif cont[0] == 'n':
            y = 2
            x = 2
        else:
            print('ERROR: please choose answer the question appropriatly')
print('OUTPUT Goodbye!\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
