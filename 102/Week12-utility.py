# Carter Strate
# CSCI 102 - Section D
# Week 12 - Utilty using Git and Increment Development
# References: rookieslab.com for some help on the prime function
# Time: TBD

def load_file(file):
    with open(file,'r') as text:
        out = text.read().split('\n')
        return out

def update_string(string1,string2,index):
    out = string1[:index]+string2+string1[index+1:]
    print(f'OUTPUT {out}')

def find_word_count(text,word):
    tcount = 0
    for line in text:
        tcount += line.count(word)
    return tcount

def score_finder(names,scores,person):
    lower_names = []
    lower_person = person.lower()
    for name in names:
        lower_name = name.lower()
        lower_names.append(lower_name)
    i = 0
    for x in lower_names:
        if x == lower_person:
            break
        i += 1
    if lower_person in lower_names:
        person = names[i]
        print(f'OUTPUT {person} got a score of {scores[i]}')
    else:
        print('OUTPUT player not found')

def union(l1,l2):
    out = l1 + l2
    return out

def intersect(l1,l2):
    out = []
    for element in l1:
        if element in l2:
            out.append(element)
    return out
def not_in(l1,l2):
    out = []
    for element in l1:
        if element not in l2:
            out.append(element)
    return out
def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True
