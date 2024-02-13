import MathFunction

def createlabelcode(labels_array):
    # print(labels_array)
    labels_list = ['None']
    for label in labels_array:
        # print(label)
        if(MathFunction.checkElementinArray(label,labels_list) == 0):
            labels_list.append(label)
    # for label in labels_list:
        # print(label)
    label_codes_list = []
    for i in range(0, len(labels_list)):
        label_codes_list.append(i)
    return labels_list, label_codes_list

def searchlabelindex(key_label,labels_list):
    index = -1
    for i in range(0,len(labels_list)):
        if(labels_list[i] == key_label):
            index = i
    return index
