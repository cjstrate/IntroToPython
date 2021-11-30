# Carter Strate
# CSCI 102 - Section D
# Week 9A - Word Search
# References: None
# Time: 10 minutes
import random
length = int(input('Enter the length of the words to find:\nLENGTH> '))# Input the length of string the user is looking for
seed = input('Enter the seed to use:\nSEED> ')# Input the seed for the random selection of word from list
f = open('dictionary.txt','r')# Open file
word_list = []
for word in f.readlines():# read through file without \n and append appropriate words to list
    if len(word) == length+1:
        word_list.append(word)
num_words = len(word_list)# take the len of the list to see how many words were of the right length
print(f'The number of words with length {length} is:\nOUTPUT {num_words}')
if num_words > 0:# If there are any words print this
    random.seed(seed)
    rand_word = random.choice(word_list)
    print(f'Here is one random word with the length {length}:\nOUTPUT {rand_word}')
else:# If there were no words print this instead
    print(f'There are no words of length {length} in the dictionary.\nOUTPUT None')
f.close()# Close the file
