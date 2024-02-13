import CSVCSVReader
import FolderLister
import MathFunction as math


def generate_series(array,n_element):
    series = []
    for i in range(0, len(array) + 1 - n_element):
        serie = []
        for j in range(i, i + n_element):
            serie.append(array[j])
        series.insert(i,serie)
    return series

def generate_serie_variance(series):
    variance_serie_array = []
    for i in range(0,len(series)):
        variance_serie = 0.0
        variance_serie = math.calculateAverageVariance(series[i])
        variance_serie_array.append(float(variance_serie))
    return variance_serie_array

def get_n_biggest_variance(variance_array):
    for i in range(0, len(variance_array)):
        variance_array.append(i)

def get_extracted_data_arrays(data_array, n_element, n_series):
    intensity_series = generate_series(data_array, n_element)
    intensity_variance_series = generate_serie_variance(intensity_series)
    intensity_variance_series, index_variance_array = math.arrange_descending_float_array(intensity_variance_series)
    # print(intensity_variance_series)
    # print(index_variance_array)
    selected_index_variance_array = []
    for i in range(0,n_series):
        selected_index_variance_array.append(int(index_variance_array[i]))
    # print(selected_index_variance_array)
    selected_index_variance_array, null = math.arrange_ascending_float_array(selected_index_variance_array)
    # print(selected_index_variance_array)

    selected_index_array = []
    for selected_index_variance_element in selected_index_variance_array:
        for i in range(0,n_element):
            selected_index_array.append(int(selected_index_variance_element + i))
    # print(selected_index_array)

    selected_index_array = math.list_elements_in_array(selected_index_array)
    # print(selected_index_array)

    return selected_index_array

def generate_intensity_series(n_element, n_selected_series):
    dataset_folder_name = 'dataset'
    source_link = 'C:/Users/Admin/Desktop/FastAccess/Fast Access/CÔNG VIỆC/TIẾN SĨ/Mau du lieu/Method 3/'
    listfile = FolderLister.listfile(source_link, dataset_folder_name)
    dataset_selected_index_array = []
    for i in range(0, len(listfile)):
        data_array = []
        intensity_series = []
        data_array = CSVCSVReader.get_intensity_data(source_link + dataset_folder_name + '/', listfile[i])
        selected_index_array = get_extracted_data_arrays(data_array,n_element,n_selected_series)
        for selected_index_element in selected_index_array:
            dataset_selected_index_array.append(selected_index_element)

    # print(dataset_selected_index_array)
    dataset_selected_index_array, null = math.arrange_ascending_float_array(dataset_selected_index_array)
    # print(dataset_selected_index_array)
    dataset_selected_index_array = math.list_elements_in_array(dataset_selected_index_array)
    return dataset_selected_index_array

def store_dataset_selected_index_array(dataset_selected_index_array):
    stored_file = open("AnomalyWaveshiftSeriesIndex.txt",'w')
    stored_array = dataset_selected_index_array
    for stored_element in stored_array:
        stored_file.write(str(stored_element))
        stored_file.write('\n')

def main():
    n_element = 10
    n_selected_series = 500
    dataset_selected_index_array = generate_intensity_series(n_element, n_selected_series)
    store_dataset_selected_index_array(dataset_selected_index_array)
    # print(dataset_selected_index_array)
    # print(len(dataset_selected_index_array))

main()