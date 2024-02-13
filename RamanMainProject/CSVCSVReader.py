import csv
import numpy as np

# Hàm này kiểm tra một số là số âm, số dương hay số 0
def check_unsigned_value(value):
    float_value = float (value)
    if(float_value > 0):
        return 1                    # Nếu là số dương thì trả về 1
    if(float_value < 0):
        return -1                   # Nếu là số âm thì trả về -1
    else:
        return 0                    # Nếu là số 0 thì trả về 0

def read_CSV_file(source_link,filename):
    with open(source_link + filename) as f:
        reader = csv.reader(f)
        # for row in reader:
        #     print(row)
        lines = [row for row in reader]
    return lines

def get_all_data(source_link,filename):
    array_waveshift = []
    array_intensity = []

    l = read_CSV_file(source_link,filename)
    i = 0
    for row in l:
        if(i!=0):
            if(check_unsigned_value(row[0]) != -1):
                # print(row[0])
                array_waveshift.append(float(row[0])) # Waveshift
                # print(row[1]) # Intensity
                array_intensity.append(int(row[1]))  # Intensity
        i += 1
    return array_waveshift, array_intensity

def get_waveshift_data(source_link,filename):
    array_waveshift = []
    l = read_CSV_file(source_link,filename)
    i = 0
    for row in l:
        if(i!=0):
            if(check_unsigned_value(row[0]) != -1):
                # print(row[0])
                array_waveshift.append(float(row[0])) # Wave Shift
        i += 1
    return array_waveshift

def get_intensity_data(source_link,filename):
    array_intensity = []
    l = read_CSV_file(source_link,filename)
    i = 0
    for row in l:
        if(i!=0):
            if (check_unsigned_value(row[0]) != -1):
                # print(row[0])
                # array_intensity.append(int(row[1]))  # Intensity
                array_intensity.append(float(row[1]))  # Intensity
        i += 1
    return array_intensity

def main():
    source_link = 'C:/Users/Admin/Desktop/FastAccess/Fast Access/CÔNG VIỆC/TIẾN SĨ/Mau du lieu/Main/File CSV/'
    csv_filename = '05M-300s100mw-1.csv'
    array_waveshift, array_intensity = get_all_data(source_link,csv_filename)
    array_waveshift = get_waveshift_data(source_link,csv_filename)
    n = len(array_waveshift)
    for i in range (0,n):
        print(f"No { (i+1) }  Waveshift: { array_waveshift[i] } Intensity: { array_intensity[i] }")

# main()