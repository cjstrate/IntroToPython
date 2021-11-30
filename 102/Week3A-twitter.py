# Carter Strate
# CSCI102 - D
# Week 3 - LabA - Twitter Decoding
# Reference: Zybooks to get beggining of code
# Time: 5 minutes

tweet = input('Enter the Tweet of Message abbreviation to decode.\nTWEET> ')

if tweet == 'LOL':
    print('The decoded abbreviation is:\nOUTPUT LOL = laughing out loud')
elif tweet == 'BFN':
    print('The decoded abbreviation is:\nOUTPUT BFN = bye for now')
elif tweet == 'FTW':
    print('The decoded abbreviation is:\nOUTPUT FTW = for the win')
elif tweet == 'IRL':
    print('The decoded abbreviation is:\nOUTPUT IRL = in real life')
elif tweet == 'IDK':
    print("The decoded abbreviation is:\nOUTPUT IDK = I don't know")
elif tweet == 'BTW':
    print('The decoded abbreviation is:\nOUTPUT BTW = by the way')
elif tweet == 'DM':
    print('The decoded abbreviation is:\nOUTPUT DM = direct message')
elif tweet == 'AFAIK':
    print('The decoded abbreviation is:\nOUTPUT AFAIK = as far as I know')
elif tweet == 'LMK':
    print('The decoded abbreviation is:\nOUTPUT LMK = let me know')
else:
    print("Sorry, don't know that one")
