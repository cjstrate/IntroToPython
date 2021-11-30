# Carter Strate
# CSCI 102- Section D
# Week 4 - Lab B - Amino Acids
# Referenes: Assighnment for formatting
# Time: 30 minutes
print('Input the chemical elements of the amino acid:')
numC = int(input('CARBON>'))
numH = int(input('HYDROGEN>'))
numN = int(input('NITROGEN>'))
numO = int(input('OXYGEN> '))
numS = int(input('SULFUR> '))

if numC == 3:
    if numS == 1:
        amino = 'Cysteine'
    elif numS == 0:
        amino = 'Alanine'
if numC == 6:
    if numH == 14:
        amino = 'Arginine'
    elif numH == 9:
        amino = 'Histidine'
if numC == 4:
    amino = 'Asparagine'
if numC == 5:
    amino = 'Glutamine'

print(f'The amino acid for {numC}C--{numH}H--{numN}N--{numO}O--{numS}S is {amino}\nOUTPUT {numC}C--{numH}H--{numN}N--{numO}O--{numS}S\nOUTPUT {amino}')
