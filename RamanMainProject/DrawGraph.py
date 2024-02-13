import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import pybaselines as pbl
import statistics

def Draw_Many_Graph(source, list_file_names, x_label, y_label, title, x_step):
    list_file_names = [str(x) for x in list_file_names]
    for i in range(len(list_file_names)):
        if len(list_file_names[i]) == 3:
            list_file_names[i] = 'Scan00' + list_file_names[i]
        if len(list_file_names[i]) == 4:
            list_file_names[i] = 'Scan0' + list_file_names[i]
    plt.figure()
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'olive', 'black', 'cyan', 'magenta', 'yellow']
    index = 0
    for i in list_file_names:
        temp = i + '.csv'
        plt.plot(GetDataFromFileCSV(source, temp, 'x'), GetDataFromFileCSV(source, temp, 'y'),
                 color=colors[index], label=i)
        index += 1
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(x_axit[::x_step], rotation='vertical')
    plt.legend()

def save_graph(location, file_name):
    plt.savefig(location+'/'+ file_name)
def Draw_Graph(x_axit, y_axit, x_label, y_label, graph_name, color, line_name):
    plt.figure()
    plt.plot(x_axit, y_axit, color=color, label=line_name)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(graph_name)
    plt.xticks(x_axit[::50],  rotation='vertical')
    plt.legend()
def Clear_drop(list):
    if min(list) < list[-1]:
        max_before = 0.0
        max_after = 0.0
        for i in range(list.index(min(list)), len(list)):
            if i+1 < len(list):
                if list[i] > list[i+1]:
                    max_after = list[i]
                    break
        for i in reversed(range(0, list.index(min(list)))):
            if i-1 > 0:
                if list[i] > list[i-1]:
                    max_before = list[i]
                    break
        for i in range(list.index(max_before)+1, list.index(max_after)):
            list[i] = max_after+(max_before-max_after)*(list.index(max_after)-i)/(list.index(max_after)-list.index(max_before))
        return list
    else:
        return list

def ReadDataTextFile(link, filename):
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
def FindPeak(list):
    peaks = []
    peaks.append(0)
    for i in range(1, len(list) - 1):
        if list[i] > list[i - 1] and list[i] > list[i + 1]:
            peaks.append(i)
        else: peaks.append(0)
    peaks.append(len(list)-1)
    return peaks

def FileName(link):
    all_file_name = os.listdir(link)
    return all_file_name

def GetDataFromFileCSV(source, filename, axit):
    datay = []
    datax = []
    with open(f'{source}/{filename}', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            if row[0] != "":
                datax.append(int(row[0]))
                datay.append(float(row[1]))
    if axit == 'x':
        return datax
    if axit == 'y':
        return datay

def CutDataByIndex(list, start, stop, max_x_axit):
    result = []
    for x in list:
        if list.index(x) >= start - (max_x_axit - len(list)) and list.index(x) <= stop - (max_x_axit - len(list)):
            result.append(x)
    return result

def RemoveBacKGround(yaxit, xaxit):
    base_line_data = pbl.polynomial.imodpoly(yaxit, xaxit, 8)
    base_line = base_line_data[0]
    result = []
    for i in range(len(base_line)):
        result.append(yaxit[i] - base_line[i])
    return result

def TotalProcessData(source, filename, title, color):
    data_y = GetDataFromFileCSV(source, filename, 'y')
    data_x = GetDataFromFileCSV(source, filename, 'x')
    data_re_back = RemoveBacKGround(data_y, data_x)
    data_cut = CutDataByIndex(data_re_back, 800, 1801, 2300)
    x_axit = np.arange(800, 800 + len(data_cut))
    plt.plot(x_axit, data_cut, color=color, label=title)
    plt.xticks(x_axit[::50], rotation='vertical')
    plt.legend()

def NoDrawProcessData(source, filename):
    data_y = GetDataFromFileCSV(source, filename, 'y')
    data_x = GetDataFromFileCSV(source, filename, 'x')
    data_re_back = RemoveBacKGround(data_y, data_x)
    data_cut = CutDataByIndex(data_re_back, 800, 1801, 2300)
    return data_cut
def SaveFlattenData(dir, filename, datay, datax):
    locate = dir + '/' + filename
    data_convert = [str(x) for x in datay]
    data = []
    for i in range(len(datay)-1):
        temp = []
        temp.append(datax[i])
        temp.append(datay[i])
        data.append(temp)
    with open(locate, 'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def AutoName(filename):
    scan_index = filename[5:10]
    refilename = 'Scan' + scan_index + '.csv'
    return refilename

sourcelink = '16-1-2024/raw_datas'
save_sourcelink = '16-1-2024/datas'

# Rename, limit the range, remove background and save to csv file

# file = FileName(sourcelink)
# print(file)
# for i in file:
#     print(AutoName(i))
#     data_temp = NoDrawProcessData(sourcelink, i)
#     datax = np.arange(800,1801)
#     SaveFlattenData(save_sourcelink, AutoName(i), data_temp, datax)
#     data_temp.clear()

# Open file, read data and draw graphs

reopen_file = FileName('16-1-2024/2_datas_labels_anhHuy/datas')
x = []
y = []
for i in reopen_file:
    x.clear()
    y.clear()
    x = GetDataFromFileCSV(save_sourcelink, i, 'x')
    y = GetDataFromFileCSV(save_sourcelink, i, 'y')
    Draw_Graph(x, y, 'Wave', 'Intense', i, 'r', i)
# break
# sourcelink2 = '26_12_2023/flatten_data_files'
#
# filename = [1029, 1032, 1033, 1034, 1064, 1065, 1066, 1067, 1068, 1069]
# Draw_Many_Graph(sourcelink2, filename, 'Wave', 'Intense', 'Mẫu 2H', 10)
#
plt.show()