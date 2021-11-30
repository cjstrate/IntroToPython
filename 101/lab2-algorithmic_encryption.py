# Carter Strate
# CSCI101 - Section G
# Python Lab 2
# Time: 30 minutes
print('Input the five listst of character to be encrypted')
L1 = input('LIST1> ')
L2 = input('LIST2> ')
L3 = input('LIST3> ')
L4 = input('LIST4> ')
L5 = input('LIST5> ')

L1e = L1[-2:]+L1[:-2]
L2e = L2[:-2]
L3e = L3[len(L3)//2:]
if len(L4) == 5:
    L4e = L4[:2]+L4[4]+L4[3]+L4[2]
elif len(L4) > 5:
    L4e = L4[:2]+L4[4]+L4[3]+L4[2]+L4[5:]
L5e1 = L5[:2]
L5e2 = L5[2:]

print(f'The encrypted message is:\nOUTPUT {L5e1} {L1e}{L2e}{L3e}{L4e} {L5e2}')
