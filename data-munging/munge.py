# Place code below to do the munging part of this assignment.
f = open("data/data.txt",'r')
heading_info = set()
info = []
start = False
for line in f:
    if line.startswith("Year"):
        heading_info.add(line)
        start = True
    if start == True:
        if line[0].isnumeric():
            info.append(line)
        elif line[0].isalpha() and not line.startswith("Year"):
            break

heading_info = list(heading_info)
ele1 = heading_info[0].strip().split(" ")
heading_list = [ele for ele in ele1 if ele][:-1]
# Given that the conditions for missing data can be complicated and thus difficult to handle automatically and repeatably, we instead manually deduce the missing data
missing_data_list = ['-0.3','-0.4']
count = 0

ele2 = []
info_list = []
for ele in info:
    ele1 = ele.strip().split(" ")
    ele2.append(ele1[0])
    for num in ele1[1:-1]:
        if num:
            if num[0].isnumeric() or num.startswith("-"):
                ele2.append(format(float(num) / 100 * 1.8, ".1f"))
            elif num.startswith("*"):
                ele2.append(missing_data_list[count])
                count += 1
    info_list.append(ele2)
    ele2 = []

f1 = open("data/clean_data.csv", "w")
f1.write(",".join(heading_list))
for line in info_list:
    f1.write("\n" + ",".join(line))
f1.close()