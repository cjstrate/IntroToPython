# Carter Strate
# CSCI 102 - Section D
# Python Lab 11
# References: None
# Time: 30 minutes
import csv
def read_csv(file):
    information = []
    try:
        with open(file, 'r', encoding='utf-8') as data:
            fileReader = csv.reader(data)
            for row in fileReader:
                information.append(row)
            return information
    except:
        thing = file.split('.')
        if thing[1] != 'csv':
            print('OUTPUT Invalid file extension')
        else:
            print('OUTPUT File does not exist')
def stops_by_race(file,race):
    totalA = 0
    totalW = 0
    totalH = 0
    totalB = 0
    totalA_P = 0
    for row in file:
        if row == file[0]:
            continue
        else:
            if row[8] == 'white':
                totalW += 1
            elif row[8] == 'black':
                totalB += 1
            elif row[8] == 'hispanic':
                totalH += 1
            elif row[8] == 'asian/pacific islander':
                totalA_P += 1
            totalA += 1
    if race == 'ALL':
        resultR = totalA
    elif race == 'white':
        resultR = totalW
    elif race == 'black':
        resultR = totalB
    elif race == 'hispanic':
        resultR = totalH
    elif race == 'asian':
        resultR = totalA_P
    print(resultR)
def stops_by_sex(file,sex):
    totalAS = 0
    totalM = 0
    totalF = 0
    for row in file:
        if row == file[0]:
            continue
        else:
            if row[9] == 'male':
                totalM += 1
            elif row[9] == 'female':
                totalF += 1
            totalAS += 1
    if sex == 'male':
        resultS = totalM
    elif sex == 'female':
        resultS = totalF
    elif sex == 'ALL':
        resultS = totalAS
    print(resultS)
file = read_csv('co_aurora_2020_04_01.csv')
stops_by_race(file,'white')
stops_by_race(file,'ALL')
print('=============================')
stops_by_sex(file,'female')
stops_by_sex(file,'ALL')
