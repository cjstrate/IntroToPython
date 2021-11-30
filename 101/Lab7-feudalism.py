# Carter Strate
# CSCI 101 - Section G
# Python Lab 7
# References: My suitmate Jordan Pettyjohn and I wrote psuedocode together
# Time: 90 minutes
num_people = int(input('Input the number of people to sort:\nNUM_PEOPLE> '))
people = []
valued_people = []
# loop to get inputs and a get rid of uneeded information
for name in range(num_people):
    person = input(f'PERSON{name}> ')
    person = person.split(' ')
    person = person[0],person[1]
    people.append(person)
# loop to get the classes by it self to calculate value
for individual in people:
    classes = individual[1].split('-')
    classes.reverse()
    worth = 0
    i = 10
# Set value of upper, middle and lower and make sure earlier sections have a larger value
    for level in classes:
        if level == 'upper':
            worth = worth + (10**i)
        elif level == 'middle':
            worth = worth + 0
        elif level == 'lower':
            worth = worth - (10**i)
        i = i - 1
    per = individual[0],worth
    valued_people.append(per)
# Sort and then reverse into largest to smallest
sorted_by_name = sorted(valued_people, key=lambda per: per[0])
sorted_by_class = sorted(sorted_by_name, key=lambda per: per[1],reverse=True)
print('After sorting, the list from highest to lowest is as follows:')
# Get rid of the : on the end of the names for the output
for x in sorted_by_class:
    x = x[0]
    x = x[0:-1]
    print(f'OUTPUT {x}')
