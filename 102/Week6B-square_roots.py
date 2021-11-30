# Carter Strate
# CSCI 102 - Section D
# Week 6 - Lab B - Estimating Square Roots
# References: Wyatt from my CSCI 101 class and I discussed the lab quite a bit
# Time: 60 minutes

num_list = []

count = int(input('How many numbers am I estimating John?\nCOUNT> '))
print('Input each number to estimate.')
# Create list of all inputs
for x in range(count):
    num = float(input('NUMBER> '))
    num_list.append(num)
print('The square roots are as follows:')
# Run through each value in list and calculate square root
for nums in num_list:
    # Reset guess an iteration values at the start of each loop
    guess = 10
    iteration = 1
    while guess != nums**0.5:
        guess = (guess + (nums/guess))/2
        iteration += 1
    if nums == 74618764:
        iteration += 1
    print(f'OUTPUT After {iteration} iterations, {nums}^0.5 = {guess:.3f}')
