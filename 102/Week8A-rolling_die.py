# Carter Strate
# CSCI 102 - Section D
# References: My suitmate Jordan Pettyjohn and I discussed this lab briefly
# Time: 20 minutes
import random
num_sides = int(input('Input the number of sides of the die:\nSIDES> '))
num_rolls = int(input('Input the number of rolls to make:\nROLLS> '))
seed = int(input('Input the seed for the random generator:\nSEED> '))

results = []

random.seed(seed)

# Roll the die the inputed number of times and append to list
for i in range(num_rolls):
    results.append(random.randint(1,num_sides))

print(f'Your {num_rolls} rolls of a {num_sides}-sided die follow:')
# Run thorugh list and find all occurences of each vlaue
for x in range(1,num_sides+1):
    if x in results:
        num = results.count(x)
        print(f'OUTPUT {x} occured {num} times')
    else:
        print(f'OUTPUT {x} occured 0 times')
