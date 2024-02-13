import ArrayComparison


# print(CSV_filename)

# Hàm này có chức năng lấy nhãn từ file CSV
def getLabel(filenames):
    labels = []

    for file in filenames:
        contentname = file.split('.')[0]
        arr_filename = contentname.split("-")
        labels.append(arr_filename[0])
    return labels

def main():

    CSV_filename = ArrayComparison.getFilesList(ArrayComparison.CSV_folder_name)
    labels = getLabel(CSV_filename)
    n = len(CSV_filename)
    for i in range(0,n):
        print(f"------------{(i+1)}--------------------")
        print(f"Tên file: {CSV_filename[i]}")
        print(f"Tên nhãn: {labels[i]}")

# main()