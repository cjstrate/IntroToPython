# Carter Strate
# CSCI 101 - Section G
# Python Lab 3
# References: Assignment for fromating details
# Time: 15 minutes

hours = int(input('HOURS> '))
minutes = int(input('MINUTES> '))
hoursA = hours
minutesA = 0

minutesA = minutes - 40
if minutesA < 0:
    minutesA = minutesA + 60
    hoursA = hours - 1
    if hoursA < 0:
        hoursA = 23
if len(str(minutesA)) == 1:
    minutesA = str('0') + str(minutesA)
if len(str(hoursA)) == 1:
    hoursA = str('0') + str(hoursA)

print(f'OUTPUT {hoursA} {minutesA}')
