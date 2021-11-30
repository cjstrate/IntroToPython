# Carter Strate
# CSCI 102 - Section D
# Week 5 - LabA - Tally for Kids
# References: Assignment for formating
# Time: 15 minutes
sums = 0
nums = []
num = None

print('Enter values to add. Enter quit when done.')
# Get inputs from user and append them to list
while num != 'quit':
    nums.append(num)
    num = input('NUMBER> ')

# Add all the numbers together
for x in nums:
    if x != None:
        x = int(x)
        sums = sums + x
    
print(f'The addition of the {len(nums)-1} numbers entered is:\nOUTPUT {len(nums)-1} numbers\nOUTPUT {sums} total')
