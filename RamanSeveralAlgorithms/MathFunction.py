def caculateDivision(divident,divisor):
    # divident / divisor = quotient and remainder
    i = 0
    while((i * divisor) <= divident):
        i+=1
    quotient = i - 1
    remainder = divident - (quotient * divisor)
    return quotient, remainder

def calculateSum(array):
    sum = 0
    for element in array:
        sum += element
    return sum

def calculateAverage(array):
    return calculateSum(array)/len(array)

def checkElementinArray(key_element, array):
    is_find = 0
    for element in array:
        if(element == key_element):
            is_find = 1
    return is_find

def calculateAverageVariance(array):
    average = calculateAverage(array)
    variance_array = []
    for element in array:
        variance_array.append((average - element) * (average - element))
    # print(variance_array)
    return calculateAverage(variance_array)

def arrange_descending_float_array(targeted_array):
    index_array = []
    for i in range(0, len(targeted_array)):
        index_array.append(int(i))

    for i in range(0, len(targeted_array)):
        for j in range (0, len(targeted_array)-i-1):
            if(float(targeted_array[j]) < float(targeted_array[j+1])):
                temp = targeted_array[j+1]
                targeted_array[j + 1] = targeted_array[j]
                targeted_array[j] = temp

                temp = index_array[j+1]
                index_array[j + 1] = index_array[j]
                index_array[j] = temp

    return targeted_array, index_array

def arrange_ascending_float_array(targeted_array):
    index_array = []
    for i in range(0, len(targeted_array)):
        index_array.append(int(i))

    for i in range(0, len(targeted_array)):
        for j in range (0, len(targeted_array)-i-1):
            if(float(targeted_array[j]) > float(targeted_array[j+1])):
                temp = targeted_array[j+1]
                targeted_array[j + 1] = targeted_array[j]
                targeted_array[j] = temp

                temp = index_array[j+1]
                index_array[j + 1] = index_array[j]
                index_array[j] = temp

    return targeted_array, index_array

def test_arrange_descending_float_array():
    # Test function arrange_descending_float_array
    array = [0.4, 0.8, 0.1, 1.5, 1.92, 2.3, 0.1, 0.3, 0.2]
    array, indexarray = arrange_descending_float_array(array)
    print(array)
    print(indexarray)

def list_elements_in_array(array):
    elements_list = []
    for element in array:
        if(checkElementinArray(element,elements_list) == 0):
            elements_list.append(element)
    return elements_list

def test_list_elements_in_array():
    # Test function arrange_descending_float_array
    array = [1, 1, 3, 4, 4, 6, 7, 9, 8]
    elements_list = list_elements_in_array(array)
    print(elements_list)

def select_element_based_on_index(array, selected_index_array):
    selected_array = []
    for index in selected_index_array:
        if(int(index) < len(array)):
            selected_array.append(array[int(index)])
    return selected_array

def test_select_element_based_on_index():
    array = [10,20,30,40,50,60,70,80,90,100,110]
    selected_index_array = [0,4,6,17]

    selected_array = select_element_based_on_index(array, selected_index_array)
    print(selected_array)

def main():
    # test_arrange_descending_float_array()
    # test_list_elements_in_array()
    test_select_element_based_on_index()

# main()