# Carter Strate
# CSCI 102 - Section D
# Week 12 - Utilty using Git and Increment Development
# References: None
# Time: TBD

def load_file(file):
    with open(file,'r') as text:
        return text.read().split('\n')

def update_string(string1,string2,index):
    out = string1[:index]+string2+string1[index+1:]
    print(f'OUTPUT {out}')

def find_word_count(file,word):
    tcount = 0
    text = load_file(file)
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
        print(f'OUTPUT {person} got a score of {scores[i]}')
    else:
        print('OUTPUT player not found')

def union(l1,l2):
    out = l1 + l2
    return out
