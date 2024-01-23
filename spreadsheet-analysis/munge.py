# place your code to clean up the data file below.
import csv

fin = open('data/Student_Weight_Status_Category_Reporting_Results__Beginning_2010.csv','r')
reader = csv.reader(fin)
fout = open('data/clean_data.csv','w', newline='')
writer = csv.writer(fout)

writer.writerow(next(reader) + ['Total (Estimated) Number of Students'])
for row in reader:
    if row[12] != '' and row[13] != '':
        new_value = round(int(row[12]) / float(row[13]))
    elif row[9] != '' and row[10] != '':
        new_value = round(int(row[9]) / float(row[10]) / 100)
    else:
        new_value = ''       
    row.append(new_value)
    writer.writerow(row)

fin.close()
fout.close()