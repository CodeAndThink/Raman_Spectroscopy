import numpy as np
import pandas as pd
from sklearn.metrics import classification_report
from tensorflow import keras

# Get datas from files
sourcelink = 'Ten_labels'
data_file_name = 'Tenlabels_RamanData'
label_file_name = 'Tenlabels_labels'

data = pd.read_csv(sourcelink + '/' + data_file_name + '.csv', header=None)
data = data.to_numpy()
target = pd.read_csv(sourcelink + '/' + label_file_name + '.csv')['has_DM2']
target = np.array([int(x) for x in target])

list_true_false = []
list_after_predict = []

for i in range(len(data)):
    test_data = data[i]
    test_label = target[i]

    #Reshape datas
    data_reshaped = test_data.reshape(1, 2048, 1)
    loaded_model = keras.models.load_model('Ten_labels/Save_model/model.h5')

    model_prediction = loaded_model.predict(data_reshaped)
    result = np.argmax(model_prediction, axis=1)
    list_after_predict.append(result[0])
    if result == test_label:
        list_true_false.append(1)
    else:
        list_true_false.append(0)
print(list_true_false)
num_true = 0
num_false = 0
for i in list_true_false:
    if i == 0:
        num_false+=1
    else:
        num_true+=1
print('Number true: ', num_true)
print('Number false: ', num_false)
print(target)
print(list_after_predict)
report = classification_report(target, list_after_predict)
print(report)