# Carter Strate
# CSCI 101 - Section B
# Python Lab 10
# References: Classmates in 101 for starting points
# Time: 60 minutes
import csv
data = []
final = []
file = input('Enter the name of the file containing the math problems.\nMATHFILE> ')
with open(file,'r') as math:
    fileReader = csv.reader(math)
    for row in fileReader:
        data.append(row)
for line in data:
    i = 0
    result = None
    for char in line:
        if char == '+':
            if result == None:
                result = int(line[i-1]) + int(line[i+1])
            else:
                result = result + int(line[i+1])
        elif char == '/':
            if result == None:
                result = int(line[i-1]) / int(line[i+1])
            else:
                result = result / int(line[i+1])
        elif char == '*':
            if result == None:
                result = int(line[i-1]) * int(line[i+1])
            else:
                result = result * int(line[i+1])
        elif char == '-':
            if result == None:
                result = int(line[i-1]) - int(line[i+1])
            else:
                result = result - int(line[i+1])
        i += 1
    if result == None:
        result = int(line[0])
    result = int(round(result,0))
    final.append(result)
outFile = input('Enter the name of the file in which to store the results.\nOUTPUTFILE> ')
with open(outFile,'w') as file_out:
    filewriter = csv.writer(file_out)
    filewriter.writerow(final)
