# Carter Strate
# CSCI 101 Section G
# Python Lab 9
# References: Ariel in my calc class for debugging
# Time: 35 minutes
print('Would you like to print the number of times a specific word appears OR print the number of words of a specifc length? (1 or 2)')
choice = int(input('CHOICE> '))
f = open('Declaration_of_independence.txt','r') # open the file
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' # define all the punctuation marks
total_list = []
word_list = []
word_listU = []
if choice == 1:
    word = input('Enter a word\nWORD: ')
    for elem in word:
        if elem in punc:
            word = word.replace(elem,'') # Remove punctuation from input
    lword = word.lower() # make input lower case
if choice == 2:
    length = int(input('Enter a length:\nLENGTH> '))
for words in f.readlines():
    for characters in words:
        if characters in punc:
            words = words.replace(characters,'')
    words = words.lower()
    words = words.split()
    total_list.append(words) # Entire loop is for reading the file getting rid of the punctuation making everything lower case and then appending everything to a list
for line in total_list:
    for words in line:
        if choice == 1:
            if words == lword:
                word_list.append(words) # Iterates through entire decleartion adding words that match the input to a list
        if choice == 2:
            if len(words) == length:
                if words.isdigit(): # If the 'word' is actually a number (1776) then ignore it
                    continue
                elif words.isalpha():
                    if words in word_listU: # If the word is of correct length append it to a list
                        word_list.append(words)
                    elif words not in word_listU:
                        word_list.append(words) # If the word is of correct length and the program has never seen it before add it to the regular list and to the unique word list
                        word_listU.append(words)
num_words = len(word_list)
if choice == 1:
    print(f'The number of times {word} appears in the document is:\nOUTPUT {num_words}')
if choice == 2:
    num_wordsU = len(word_listU)
    print(f'The number of words in the document with length {length} is:\nOUTPUT {num_words}')
    print(f'The number of unique words in the document with length {length} is:\nOUTPUT {num_wordsU}')
f.close()
# General output formating and make sure to close the file
