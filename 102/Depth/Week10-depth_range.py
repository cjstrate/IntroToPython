# Carter Strate
# CSCI 102 - Section D
# Week 10 Lab
# References: None
# Time: 40 minutes
import csv
l = []
with open('formations.csv','r') as file:
    fileReader = csv.reader(file)
    for row in fileReader:
        l.append(row)
for line in l:
    if line == l[0]:
        line.insert(1,'Start Depth')
        line.insert(2,'End Depth')
        line.insert(3,'Difference in Depth')
    else:
        depths = line[0]
        depths = depths.split('-')
        sDepth = float(depths[0])
        fDepth = float(depths[1])
        dDepth = '{:.2f}'.format(round(fDepth - sDepth,2))
        line.insert(1,sDepth)
        line.insert(2,fDepth)
        line.insert(3,dDepth)
with open('formations_parsed.csv','w') as fileP:
    filePwriter = csv.writer(fileP)
    for line in l:
        filePwriter.writerow(line)
