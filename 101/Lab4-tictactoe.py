# Carter Strate
# CSCI 101 - Section G
# Python Lab 4
# References: None
# Time: 15 minutes

row0 = input('ROW0> ')
row1 = input('ROW1> ')
row2 = input('ROW2> ')

if row0[0] == row1[1] == row2[2]:
    winner = row0[0]
    print(winner)
elif row0[0] == row1[0] == row2[0]:
    winner = row0[0]
elif row0[1] == row1[1] == row2[1]:
    winner = row0[1]
elif row0[2] == row1[2] == row2[2]:
    winner = row0[2]
elif row0[2] == row1[1] == row2[0]:
    winner = row0[2]
elif row0[0] == row0[1] == row0[2]:
    winner = row0[0]
elif row1[0] == row1[1] == row1[2]:
    winner = row1[0]
elif row2[0] == row2[1] == row2[2]:
    winner = row2[0]
else:
    winner = 'N'

if winner == 'E':
    winner = 'N'
    
print(f'OUTPUT {winner}')
