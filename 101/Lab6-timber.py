# Carter Strate
# CSCI 101 - Section G
# Python Lab 6: Timber Regrowth
# References: None
# Time: 10 minutes

years = int(input('Input the number of years to print in the reforestation table:\nYEARS> '))

num_acres = 3000
reforest_rate = 0.03
acres_available = 12000
year = 0

print('The reforestation table is then\nYear, # Acres, % Forest')
print('OUTPUT 0, 3000.0, 25.00%')
for time in range(1,years+1):   
    num_acres = num_acres + (num_acres * reforest_rate)
    forest_percent = (num_acres / acres_available) * 100
    print(f'OUTPUT {time}, {num_acres:.1f}, {forest_percent:.2f}%')
forest_percent = 0
num_acres = 3000
acres_available
while forest_percent < 100:
    num_acres = num_acres + (num_acres * reforest_rate)
    forest_percent = (num_acres / acres_available) * 100
    year += 1
print(f'OUTPUT {year}')
