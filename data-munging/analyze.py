# Place code below to do the analysis part of the assignment.

import csv

f = open('data/clean_data.csv','r')
csv_reader = csv.DictReader(f)
title_identifier = True
count = 0
sum_decade = 0
print("Average Temperature Anomaly in Degrees Farenheit for Each Decade Since 1880:")

for line in csv_reader:   
    if count == 9:
        sum_decade += float(line["J-D"])
        average_decade = format(sum_decade/10,".2f")
        year_end = line["Year"]
        print(f'{year_begin} to {year_end}: {average_decade}')            
        count = 0
        sum_decade = 0
        average_decade = 0
        continue
    if count == 0:
        year_begin = line["Year"]
    count += 1
    sum_decade += float(line["J-D"])

if count != 9:
    year_begin = str(int(year_end) + 1)
    year_end = str(int(year_begin) + count - 1)
    average_decade = format(sum_decade/count,".2f")
    print(f'{year_begin} to {year_end}: {average_decade}')
