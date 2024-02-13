import csv
import os

source_link = 'C:/Users/Admin/Desktop/FastAccess/Fast Access/CÔNG VIỆC/TIẾN SĨ/Mau du lieu/Main/'
TXT_folder_name = 'File Text'
CSV_folder_name = 'File CSV'

def findmaxvalue (array):
    max_value = 0
    for value in array:
        int_value = float(value)
        if(int_value >= max_value):
            max_value = int_value
    return max_value

def findminvalue (array,max_value):
    min_value = max_value
    for value in array:
        int_value = float(value)
        if(int_value <= min_value):
            min_value = int_value
    return min_value

# Hàm này có mục đích là kiểm tra xem hai mảng giống nhau hay là khác nhau
def checkArrayDifference (array1, array2):
                                            # check_flag = 1: Hai mảng giống hệt nhau
                                            # check_flag = 0: Hai mảng khác nhau
                                            # print(array1)
                                            # print(array2)
    check_flag = 1
    if (len(array1) != len(array2)):
        check_flag = 0
    else:
        for i in range(0,len(array1)):
            value1 = float(array1[i])
            value2 = float(array2[i])

            if((value1 - value2) != 0):
                check_flag = 0
    return check_flag

def getCSVDatatoArrray (csv_filename):
    waveshiftarray = []
    intensityarray = []
    with open(source_link + CSV_folder_name + '/' + csv_filename) as f:
        reader = csv.reader(f)
        # for row in reader:
        #     print(row)
        l = [row for row in reader]
    for row in l:
        # print(row[0])
        # print(row[1])
        waveshiftarray.append(row[0])
        intensityarray.append(row[1])
    return waveshiftarray[1:], intensityarray[1:]

def getTXTDatatoArrray (text_filename):
    waveshiftarray = []
    intensityarray = []
    f = open(source_link + TXT_folder_name + '/' + text_filename, 'r')
    if f.mode == 'r':
        f1 = f.readlines()
        for str_data in f1:
            # print(str_data)
            data_list = str_data.split()
            waveshiftarray.append(data_list[0])
            intensityarray.append(data_list[1])
    else:
        print('Can not read file')
    return waveshiftarray, intensityarray

def getFilesList(folder_name):
    filesList = []
    n = 0
    for filename in os.listdir(source_link + folder_name):
        n += 1
        filesList.append(filename)
    return filesList

def main():
    wrongfile = []

    TXT_filenamelist = getFilesList(TXT_folder_name)
    # print(TXT_filenamelist)

    CSV_filenamelist = getFilesList(CSV_folder_name)
    # print(CSV_filenamelist)

    n = len(TXT_filenamelist)
    print(f"Có tổng cộng {n} File dữ liệu")

    for i in range (0,n):
        print(f"----------------{(i+1)}------------")
        check_flag = 1
        CSV_waveshiftarray = []
        CSV_intensityarray = []
        CSV_waveshiftarray, CSV_intensityarray = getCSVDatatoArrray(CSV_filenamelist[i])
        print(f"Đã upload file CSV {CSV_filenamelist[i]}")

        TXT_waveshiftarray = []
        TXT_intensityarray = []
        TXT_waveshiftarray, TXT_intensityarray = getTXTDatatoArrray(TXT_filenamelist[i])
        print(f"Đã upload file TXT {TXT_filenamelist[i]}")

        if(checkArrayDifference(CSV_waveshiftarray,TXT_waveshiftarray)==0):
            check_flag = 0

        if(checkArrayDifference(CSV_intensityarray,TXT_intensityarray)==0):
            check_flag = 0

        if(check_flag == 0):
            print("Kết quả đối chứng là: SAI")
            wrongfile.append(TXT_filenamelist[i])
        else:
            print("Kết quả đối chứng là: ĐÚNG")

    print("-------------KẾT LUẬN------------")
    if(len(wrongfile)==0):
        print("Dữ liệu giữa File Txt và File CSV trùng khớp")
    else:
        print("File chuyển đổi sai giữa CSV và TXT là:")
        for filename in wrongfile:
            print(filename)

# main()