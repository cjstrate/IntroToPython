# Carter Strate
# CSCI 102 -Secion D
# Week 3 - Lab B - Enhanced Calculator
# Time: 30 min

num1 = 0.0
num2 = 0.0
sums = 0.0
diff = 0.0
product = 0.0
quotient = 0.0
remainder =  0.0

print('Welcome to our Enhanced Calculator!')
num1 = float(input('Input the first operand.\nFIRST> '))
num2 = float(input('Input the second operand.\nSECOND> '))

print('Choose one of the following operations:\n1 - addition\n2 - subtraction\n3 - multiplication\n4 - division')

op = int(input('OPETATION> '))

# Python automatically cuts off trailing zeroes so rouned so that there are always 6 decimal places
if op == 1:
    sums = round(num1 + num2,6)
    print(f'The results of the addition is: {sums:.6f}\nOUTPUT {sums:.6f}')
elif op == 2:
    diff = round((num1 - num2),6)
    print(f'The results of the subtraction is: {diff:.6f}\nOUTPUT {diff:.6f}')
elif op == 3:
    product = round(num1 * num2,6)
    print(f'The results of the multiplication is: {product:.6f}\nOUTPUT {product:.6f}')
# No decimal places for divisions make sure remainder and quotient are integers
elif op == 4:
    if num2 == 0:
        print('Sorry dividing by 0 is impossible')
    else:
        quotient = int(num1 // num2)
        remainder = int(num1 % num2)
        print(f'The results of the division is: {quotient} (quotient) and {remainder} (remainder)\nOUTPUT {quotient}\nOUTPUT {remainder}')
else:
    print('Please enter one of the given numbers for the operation')

print('Thank you for using our calculator.')
