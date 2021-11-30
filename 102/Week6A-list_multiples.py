# Carter Strate
# CSCI 102 - Section D
# Week 6 - Lab A - List of Multiples
# References: None
# Time: 5 minutes

num = int(input('Enter the number to create multiples for.\nNUMBER> '))
# index = index + 2 so that the range funtion will not exclude the last value
index = int(input('Enter the maximum index of the list.\nINDEX> '))+2
# out is a list containing the outputs of all the multiplication
out = []
for x in range(1,index):
    x = x * num
    out.append(x)
print(f'Your list of multiples is as follows:\nOUTPUT {out}')
