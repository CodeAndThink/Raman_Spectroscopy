import csv
import shutil
import os
import random
import pandas as pd
import numpy as np

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(int(row[0]))
    return data

def shuffle_data(data, label):
    old_index = list(range(len(data)))
    new_index = old_index.copy()
    random.shuffle(new_index)
    new_data = [data[i] for i in new_index]
    new_label = [label[i] for i in new_index]

    print('Old order: ', old_index)
    print('Old label: ', label)
    print('Old first data: ', data[0])

    print('New order: ', new_index)
    print('New label: ', new_label)
    print('New first data: ', new_data[0])
    return new_data, new_label, new_index
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

def Load_compile_data(source, filename):
    X = []
    temp = []
    with open(f'{source}/{filename}', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            temp = []
            for i in row:
                temp.append(float(i))
            X.append(temp)
    return X

def FileName(link):
    all_file_name = os.listdir(link)
    return all_file_name

def Compile_data_files(raw_datas_locate, compile_datas_locate, name_compile_datas_file):
    file_names = FileName(raw_datas_locate)
    temp = []
    for i in file_names:
        temp.append(GetDataFromFileCSV(raw_datas_locate, i, 'y'))

    locate = compile_datas_locate + '/' + name_compile_datas_file + '.csv'
    with open(locate, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(temp)

def Auto_labels(label_file_name, local_labels, local_datas, list_before_eat, list_after_eat):
    file_names = FileName(local_datas)
    list_before_eat = [str(x) for x in list_before_eat]
    for i in range(len(list_before_eat)):
        if len(list_before_eat[i]) == 3:
            list_before_eat[i] = 'Scan00' + list_before_eat[i] + '.csv'
        if len(list_before_eat[i]) == 4:
            list_before_eat[i] = 'Scan0' + list_before_eat[i] + '.csv'
    list_after_eat = [str(x) for x in list_after_eat]
    for i in range(len(list_after_eat)):
        if len(list_after_eat[i]) == 3:
            list_after_eat[i] = 'Scan00' + list_after_eat[i] + '.csv'
        if len(list_after_eat[i]) == 4:
            list_after_eat[i] = 'Scan0' + list_after_eat[i] + '.csv'
    print(list_before_eat)
    print(list_after_eat)
    temp = []
    for i in range(len(file_names)):
        if file_names[i] in list_before_eat:
            temp.append('0')
        if file_names[i] in list_after_eat:
            temp.append('1')
    print(file_names)
    print(temp)
    locate = local_labels + '/' + label_file_name + '.csv'
    with open(locate, 'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(temp)
def Auto_multi_labels(label_file_name, local_labels, local_datas, list_before_eat, list_after_eat, list_after_drink_glucose):
    file_names = FileName(local_datas)
    list_before_eat = [str(x) for x in list_before_eat]
    for i in range(len(list_before_eat)):
        if len(list_before_eat[i]) == 3:
            list_before_eat[i] = 'Scan00' + list_before_eat[i] + '.csv'
        if len(list_before_eat[i]) == 4:
            list_before_eat[i] = 'Scan0' + list_before_eat[i] + '.csv'
    list_after_eat = [str(x) for x in list_after_eat]
    for i in range(len(list_after_eat)):
        if len(list_after_eat[i]) == 3:
            list_after_eat[i] = 'Scan00' + list_after_eat[i] + '.csv'
        if len(list_after_eat[i]) == 4:
            list_after_eat[i] = 'Scan0' + list_after_eat[i] + '.csv'
    list_after_drink_glucose = [str(x) for x in list_after_drink_glucose]
    for i in range(len(list_after_drink_glucose)):
        if len(list_after_drink_glucose[i]) == 3:
            list_after_drink_glucose[i] = 'Scan00' + list_after_drink_glucose[i] + '.csv'
        if len(list_after_drink_glucose[i]) == 4:
            list_after_drink_glucose[i] = 'Scan0' + list_after_drink_glucose[i] + '.csv'
    print(list_before_eat)
    print(list_after_eat)
    print(list_after_drink_glucose)
    temp = []
    for i in range(len(file_names)):
        if file_names[i] in list_before_eat:
            temp.append('0')
        if file_names[i] in list_after_eat:
            temp.append('1')
        if file_names[i] in list_after_drink_glucose:
            temp.append('2')
    print(file_names)
    print(temp)
    locate = local_labels + '/' + label_file_name + '.csv'
    with open(locate, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(temp)
def copy_file(source_folder, destination_folder, file_name):
    source_path = os.path.join(source_folder, file_name)
    destination_path = os.path.join(destination_folder, file_name)

    try:
        shutil.copy(source_path, destination_path)
        print(f"File '{file_name}' copied successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except PermissionError:
        print(f"Permission error. Check if you have the required permissions.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
source_folder = '16-1-2024/datas'
destination_folder = '16-1-2024/datas'
label_folder = '16-1-2024/labels'
data_folder = '16-1-2024/compile_datas'
data_file_name = 'datas.csv'
label_file_name = 'labels.csv'
destination_folder_truong = '16-1-2024/2_datas_labels_truong'
label_folder_truong = '16-1-2024/2_datas_labels_truong'

# list_file_names = [1006, 1007, 1008,993, 994, 995,1015, 1016, 1017, 1018,1023, 1024, 1025, 1009, 1010, 1011, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005,
# 1012, 1013, 1014, 1020, 1021, 1022,1026, 1027, 1028, 1041, 1042, 1043, 1057, 1058, 1059, 1035, 1036, 1037, 1044, 1045, 1046, 1051, 1052, 1053, 1054, 1055, 1056, 1047,
# 1048, 1049, 1050, 1060, 1061, 1062]
list_before = [1123, 1124,1125, 1126, 1127, 1128, 1130, 1131, 1132]
list_after = [1154, 1155, 1156, 1158, 1159, 1160, 1161, 1162, 1163]
list_after_drink_glucose = [1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192, 1193]
# list_file_names = [str(x) for x in list_file_names]
# for i in range(len(list_file_names)):
#     if len(list_file_names[i]) == 3:
#         list_file_names[i] = 'Scan00' + list_file_names[i]
#     if len(list_file_names[i]) == 4:
#         list_file_names[i] = 'Scan0' + list_file_names[i]
#
# for i in list_file_names:
#     file_name = i + '.csv'
#     copy_file(source_folder, destination_folder, file_name)
#
# Auto_labels('labels','16-1-2024/2_datas_labels_anhHuy', '16-1-2024/2_datas_labels_anhHuy/datas', list_before, list_after)
# Auto_multi_labels('labels','16-1-2024/3_datas_labels_truong', '16-1-2024/3_datas_labels_truong/datas', list_before, list_after, list_after_drink_glucose)
# Compile_data_files('16-1-2024/3_datas_labels_truong/datas', '16-1-2024/3_datas_labels_truong', 'datas')


#
# raw_data = Load_compile_data(data_folder, data_file_name)
# raw_data = np.array(raw_data)
# raw_labels = read_csv_file(label_folder + '/' + label_file_name)
# raw_labels = np.array([int(x) for x in raw_labels])
# print(raw_data)
# print(raw_labels)
# print(raw_data)
#
# after_shuffle_datas, after_shuffle_labels, new_labels_order = shuffle_data(raw_data, raw_labels)