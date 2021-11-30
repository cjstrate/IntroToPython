#Carter Strate
#CSCI 102-Section D
#Week 2 - Part A
#References: Assignment details for formating
#Time: 12 minutes

# Input 1
num1 = 0.0
# Input 2
num2 = 0.0

sums = 0.0
diff = 0.0
product = 0.0
quotient = 0.0
remainder = 0.0

#Follow very specific formatting
num1 = float(input('Input the firts operand\nFIRST> '))
num2 = float(input('Input the second operand\nSECOND> '))

sums = round(num1+num2,1)
diff = round(num1-num2,1)
product = round(num1*num2,1)
# quotient needs to be an integer not rounded to 0 decimal places
quotient = int(num1//num2)
remainder = round(num1%num2,2)

print(f'\nThe sum of {num1} and {num2} is {sums}\nOUTPUT {sums}')
print(f'The difference of {num1} and {num2} is {diff}\nOUTPUT {diff}')
print(f'The product of {num1} and {num2} is {product}\nOUTPUT {product}')
print(f'The quotient of {num1} and {num2} is {quotient}\nOUTPUT {quotient}')
print(f'The remainder of {num1} and {num2} is {remainder}\nOUTPUT {remainder}')
