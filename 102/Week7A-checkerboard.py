# Carter Strate
# CSCI 102 - Section D
# Week 7 - Lab A - Checkerboard
# References: None
# Time: 45 minutes
rows = int(input('How many rows does the checkerboard have?\nROWS> '))
columns = int(input('How many columns does the checkerboard have?\nCOLUMNS> '))
print('What are the strings with which to pattern it?')
element_a = input('FIRST> ')
element_b = input('SECOND> ')

l1 = []
l2 = []

# Make a list with the number of columns as the number of values in the list of a,b and b,a
if columns % 2 == 0:
    for value in range(columns//2):
        l1.append(element_a)
        l1.append(element_b)
        l2.append(element_b)
        l2.append(element_a)
# The intial loop dos not work whe columns is odd
elif columns % 2 != 0:
    for value in range(columns):
        if value % 2 == 0:
            l1.append(element_a)
            l2.append(element_b)
        elif value % 2 != 0:
            l1.append(element_b)
            l2.append(element_a)
print(f'A checkerboard with {rows} rows, {columns} columns, first string is {element_a}, and second string is {element_b} is:')
# Print appropriate lists for however many rows there are (alterante a,b and b,a)
for value in range(rows):
    if value % 2 == 0:
        print(f'OUTPUT {l1}')
    else:
        print(f'OUTPUT {l2}')
if rows == 0:
    print([])
print('And the 2D array representation is:')
lt = []
# Make a list of lists to display the two D aray (lt = list total)
for value in range(rows):
    if value % 2 == 0:
        lt.append(l1)
    else:
        lt.append(l2)
print(f'OUTPUT {lt}')
