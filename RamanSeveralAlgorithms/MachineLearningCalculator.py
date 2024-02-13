import numpy as np
from sklearn.metrics import confusion_matrix

def sensitivity(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    FP = cm.sum(axis=0) - np.diag(cm)
    FN = cm.sum(axis=1) - np.diag(cm)
    TP = np.diag(cm)
    TN = cm.sum() - (FP + FN + TP)
    Sensitivity = TP / (TP + FN)
    return np.mean(Sensitivity)


def specificity(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    FP = cm.sum(axis=0) - np.diag(cm)
    FN = cm.sum(axis=1) - np.diag(cm)
    TP = np.diag(cm)
    TN = cm.sum() - (FP + FN + TP)
    Specificity = TN / (TN + FP)
    return np.mean(Specificity)

y_test = [1,2,3,4,5,6,7,8,9,10]
y_pred = [10,9,8,7,6,5,4,3,2,1]
# [ 1  2  1  4  5  6  7  8  9 10]

def RvO_convert(label_target, array):
    converted_array = []
    for i in range(0, len(array)):
        converted_array.append(-1)

    for i in range(0, len(array)):
        # print(f"label_target", i)
        if(array[i] == label_target):
            converted_array[i] = 1
        else:
            converted_array[i] = 0
    return converted_array

def RvO_sensitivity(y_pred,y_test):
    sum_sensitivity = 0

    for i in range(1,11):
        # print(f"label_target", i)
        RvO_y_true = RvO_convert(i,y_test)
        RvO_y_prediction = RvO_convert(i, y_pred)
        TP = 0
        FP = 0
        FN = 0
        TN = 0
        for i in range(0, len(RvO_y_true)):
            if(RvO_y_true[i] == 1):
                if(RvO_y_prediction[i] == 1):
                    TP += 1
                else:
                    FN += 1
            else:
                if (RvO_y_prediction[i] == 1):
                    FP += 1
                else:
                    TN += 1
        sensitivity = TP / (TP + FN)

        # print(f"TP", TP)
        # print(f"FN", FN)
        # print(f"FP", FP)
        # print(f"TN", TN)
        # print(f"sensitivity", sensitivity)

        sum_sensitivity += sensitivity

    return (sum_sensitivity/10)

def RvO_specificity(y_pred,y_test):
    sum_specificity = 0
    for i in range(1,11):
        # print(f"label_target", i)
        RvO_y_true = RvO_convert(i,y_test)
        RvO_y_prediction = RvO_convert(i, y_pred)
        TP = 0
        FP = 0
        FN = 0
        TN = 0
        for i in range(0, len(RvO_y_true)):
            if(RvO_y_true[i] == 1):
                if(RvO_y_prediction[i] == 1):
                    TP += 1
                else:
                    FN += 1
            else:
                if (RvO_y_prediction[i] == 1):
                    FP += 1
                else:
                    TN += 1

        specificity = TN / (TN + FP)

        # print(f"TP", TP)
        # print(f"FN", FN)
        # print(f"FP", FP)
        # print(f"TN", TN)
        # print(f"specificity", specificity)
        sum_specificity += specificity

    return (sum_specificity/10)




