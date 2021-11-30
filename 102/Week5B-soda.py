# Carter Strate
# CSCI 102 - Section D
# Week 5 - Lab B - Soda Sprinter
# References: Assighnment for formatting
# Time: 20 minutes
bottlesI = int(input("Enter the number of empty bottles in Blaster's possession at the start of the day.\nEMPTIES> "))
bottlesF = int(input("Enter the numnber of empty bottles that Blaster found during the day.\nFOUND> "))
cost = int(input("Enter the number of empty bottles the Blaster needs to buy a new soda.\nCOST> "))

bottlesT = bottlesI + bottlesF
soda = bottlesT // cost
drank = soda
remainder = (bottlesT % cost) + soda
while remainder >= cost:
    drank = drank + (remainder // cost)
    remainder = (remainder % cost) + (remainder // cost)
print(f'The total number of sodas that Blaster drank is:\nOUTPUT {drank}')
