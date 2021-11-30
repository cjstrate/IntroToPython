# Carter Strate
# CSCI 102 - Section D
# Week 8 - Lab B - Combing Through a Haystack
# References: Ben in my 101 class
# Time: 40 minutes
whole_string = input('Enter a DNA string s:\ns> ')
sub_string = input('Enter a substring t:\nt> ')
length = len(whole_string)
location = ''
num = 0
x = 1
element = 0

while x == 1:
    index = whole_string.find(sub_string, element)
    if index != -1:
        location = location + ' ' + str(index+1)
        num += 1
    else:
        break
    element = index + 1

if len(sub_string) > len(whole_string):
    print(f'Error: Substring is longer than DNA string\nOUTPUT ERROR')

else:
    if num > 0:
        print(f'The total number of substrings found is {num}\nOUTPUT {num}')
        print(f'The locations of these substrings in s are: {location}\nOUTPUT {location}')
    else:    
        print(f'The total number of substrings found is 0\nOUTPUT 0')
