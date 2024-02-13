import os

# Hàm này liệt kê tất cả các file và folder của một file
def listfile(source_link, folder_name):
    n = 0
    INPUT = source_link + folder_name
    filenames = []

    for filename in os.listdir(INPUT):
        n += 1
        filenames.append(filename)
        # print(filename)
    # print(filenames)
    return filenames

def main():
    folder_name = 'File CSV'
    source_link = 'C:/Users/Admin/Desktop/FastAccess/Fast Access/CÔNG VIỆC/TIẾN SĨ/Mau du lieu/Main/'

    print('Liệt kê thư mục')
    print('----------------------------------------------')

    filenames = listfile(source_link,folder_name)

    n = 1

    for filename in filenames:
        print(filename)
        n += 1

    print('-------------------------')
    print(f"Tổng số file trong thư mục: {n}")

# main()