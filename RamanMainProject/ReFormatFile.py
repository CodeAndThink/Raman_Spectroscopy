import os
import pathlib as pl
import matplotlib.pyplot as plt
import pybaselines as pbl

def FileName(link):
    all_file_name = os.listdir(source_link)
    return all_file_name

def ReadDataFile(link, filename):
    file_name = link+"/"+filename
    ofile = open(file_name, "r")
    get_data = ofile.readlines()
    get_data = get_data[2:]
    two_d_data = []
    for i in get_data:
        i = i[1:]
        i = i.replace('\n', '')
        i = i.replace('  ', '/')
        two_d_data.append(i.split('/'))
    return two_d_data

def CompareTwoChart(link, filename1, filename2):
    first_chart = ReadDataFile(link,filename1)
    x_axit_1 = [float(i[0]) for i in first_chart]
    y_axit_1 = [float(i[1]) for i in first_chart]
    second_chart = ReadDataFile(link, filename2)
    x_axit_2 = [float(i[0]) for i in second_chart]
    y_axit_2 = [float(i[1]) for i in second_chart]

    plt.figure()
    plt.plot(x_axit_1, y_axit_1, color='b', label="First")
    plt.plot(x_axit_2, y_axit_2, color='r', label="Second")
    plt.xlabel('Index')
    plt.ylabel('Signal')
    plt.title(filename1 + " vs " + filename2)
    plt.xticks(x_axit_1[::50], rotation='vertical')
    plt.legend()

#MAIN
source_link = "C:/Users/trg14/PycharmProjects/RamanMainProject/new_data_20.11.2023"
file_name_1 = "test aimh.txt"
file_name_2 = "test aimt.txt"

file_name = FileName(source_link)
for i in file_name:
    data = ReadDataFile(source_link, i)
    x_axit_temp = [float(l[0]) for l in data]
    y_axit_temp = [float(l[1]) for l in data]

    plt.figure()
    plt.plot(x_axit_temp, y_axit_temp, color='b', label="Signal")
    plt.xlabel('Index')
    plt.ylabel('Signal')
    plt.title(i)
    plt.xticks(x_axit_temp[::50], rotation='vertical')
    plt.legend()

    first_base_line_1 = pbl.polynomial.imodpoly(y_axit_temp, x_axit_temp, 10, 0.001, 250, None, False, True, False, 0)
    second_base_line_1 = first_base_line_1[0]
    for j in range(len(second_base_line_1)):
        y_axit_temp[j] -= second_base_line_1[j]

    plt.figure()
    plt.plot(x_axit_temp, y_axit_temp, color='b', label="Signal")
    plt.xlabel('Index')
    plt.ylabel('Signal')
    plt.title(i)
    plt.xticks(x_axit_temp[::50], rotation='vertical')
    plt.legend()

# CompareTwoChart(source_link,file_name_1,file_name_2)

plt.show()
