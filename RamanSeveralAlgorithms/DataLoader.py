import FolderLister
import LabelGetter
import LabelEncode
import CSVCSVReader
import MathFunction as math

# import WaveshiftSeriesAnomalyDetection as wsad

#   Hàm này có chức năng lấy dữ liệu từ file CSV đưa vào cấu trúc list python
def loaddata(source_link, folder_name):
    X = []
    y = []
    listfile = FolderLister.listfile(source_link, folder_name)
    labels = LabelGetter.getLabel(listfile)

    # Liệt kê nhãn cũng như chuyển đổi sang mã nhãn
    labelslist, labelcodeslist = LabelEncode.createlabelcode(labels)
    print("-------Label and Label code in dataset-------")
    for i in range (0, len(labelslist)):
        print(f"Label: {labelslist[i]} with code {labelcodeslist[i]}")
    print("-----------------------")

    for i in range(0, len(listfile)):

        index = -1
        for j in range(0, len(labelslist)):
            if (labelslist[j] == labels[i]):
                index = j

        y.append(int(labelcodeslist[index]))

        data_array = []
        data_array = CSVCSVReader.get_intensity_data(source_link + folder_name + '/', listfile[i])
        for j in range(0, len(data_array)):
            data_array[j] += 0
        X.insert(i, data_array)

    return X, y

def access_dataset_selected_index_array():
    # read.py
    # loading a file with open()
    dataset_selected_index_array = []
    stored_file = open("AnomalyWaveshiftSeriesIndex.txt")
    # reading each line of the file and printing to the console
    for line in stored_file:
        dataset_selected_index_array.append(int(line))
    return dataset_selected_index_array

def loaddata_withseriesanomolydetection(source_link, folder_name):
    print("-----------Searching Anomaly series---------")
    # dataset_selected_index_array = wsad.generate_intensity_series(n_element, n_selected_series)

    dataset_selected_index_array = access_dataset_selected_index_array()

    print(dataset_selected_index_array)
    print(len(dataset_selected_index_array))
    print("-----------Search completed---------")

    X = []
    y = []
    listfile = FolderLister.listfile(source_link, folder_name)
    labels = LabelGetter.getLabel(listfile)

    # Liệt kê nhãn cũng như chuyển đổi sang mã nhãn
    labelslist, labelcodeslist = LabelEncode.createlabelcode(labels)
    print("-------Label and Label code in dataset-------")
    for i in range (0, len(labelslist)):
        print(f"Label: {labelslist[i]} with code {labelcodeslist[i]}")
    print("-----------------------")

    for i in range(0, len(listfile)):

        index = -1
        for j in range(0, len(labelslist)):
            if (labelslist[j] == labels[i]):
                index = j

        y.append(int(labelcodeslist[index]))

        data_array = []
        data_array = CSVCSVReader.get_intensity_data(source_link + folder_name + '/', listfile[i])

        data_array = math.select_element_based_on_index(data_array, dataset_selected_index_array)
        # print(data_array)

        for j in range(0, len(data_array)):
            data_array[j] += 0
        X.insert(i, data_array)

    return X, y