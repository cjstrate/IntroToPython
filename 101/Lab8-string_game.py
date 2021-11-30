# Carter Strate
# CSCI 101 - Section G
# Python Lab 8
# References: Google for various syntax for use of differnt funtios
# time: 70 minutes
import random
alpha = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
vow = 'AEIOU'
con = 'BCDFGHJKLMNPQRSTVXYZ'
kevin = 0
stacy = 0
k_pre_used = []
s_pre_used = []

choice = int(input('Would you like to provide your own string or generate a random one? (1 or 2)\nCHOICE> '))

if choice == 1:
    string = input('Enter a string for the game:\nSTRING> ')
if choice == 2:
    seed = int(input('Number to initialize the random generator:\nSEED> '))
    random.seed(seed)
    string = random.choices(alpha,k=6)
    string = ''.join(string)

i = 0
for letter in string:
    if letter in con:
        if letter in k_pre_used:
            continue
        else:
            ki = i
            kev_string = ''
            for kadd_letter in string[i:]:
                kev_string = kev_string + string[ki]
                x = 1
                kelement = 0
                while x == 1:
                    kindex = string.find(kev_string,kelement)
                    if kindex != -1:
                        kevin = kevin + 1
                    else:
                        break
                    kelement = kindex + 1
                ki = ki + 1
        k_pre_used.append(letter)
    if letter in vow:
        if letter in s_pre_used:
            continue
        else:
            si = i
            sta_string = ''
            for sadd_letter in string[i:]:
                sta_string = sta_string + string[si]
                y = 1
                selement = 0
                while y == 1:
                    sindex = string.find(sta_string,selement)
                    if sindex != -1:
                        stacy = stacy + 1
                    else:
                        break
                    selement = sindex + 1
                si = si +1
        s_pre_used.append(letter)
    i = i + 1

if choice == 1:
    print(f"With the string {string}, Kevin's score is {kevin} and Stacy's score is {stacy}")
elif choice == 2:
    print(f'The randomly generated string for this game is {string}')
    print(f"With the string {string}, Kevin's score is {kevin} and Stacy's score is {stacy}")
if kevin > stacy:
    print('Kevin wins!')
    f = 'Kevin'
elif kevin < stacy:
    print('Stacy wins!')
    f = 'Stacy'
elif kevin == stacy:
    print("It's a tie!")
    f = 'Draw'
print(f'OUTPUT {kevin}')
print(f'OUTPUT {stacy}')
print(f'OUTPUT {f}')
