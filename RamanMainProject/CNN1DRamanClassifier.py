# -*- coding: utf-8 -*-
"""conv.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FmPveI6oXlUvqpm1hMCtlEl_En7fglwF
"""

import numpy as np
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2
import random

# Import TensorBoard
from tensorflow.keras.callbacks import TensorBoard

def shuffle_data(data, label):
    print('Data shape: ', data.shape)
    print('Label shape: ', label.shape)

    old_index = list(range(len(data)))
    new_index = old_index.copy()
    random.shuffle(new_index)
    new_data = [data[i] for i in new_index]
    new_label = [label[i] for i in new_index]

    print('Old order: ', old_index)
    print('Old label: ', label)
    print('Old first data: ', data[0])

    print('New order: ', new_index)
    print('New label: ', new_label)
    print('New first data: ', new_data[0])
    return new_data, new_label, new_index

def plot_accuracy_per_fold():
    plt.plot(acc_per_fold)
    plt.title(f'Accuracy per fold for {data_file_name}')
    plt.xlabel('Fold')
    plt.ylabel('Accuracy')
    plt.legend(['Accuracy'])
    # plt.savefig(f'plot/nn_{file_name}.pdf', bbox_inches='tight')
    plt.show()

def plot_history(history):
    plt.figure()
    plt.plot(history.history['loss'], label='Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title(f'Loss for {data_file_name}')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    # plt.savefig(f'plot/loss_{data_file_name}.pdf', bbox_inches='tight')

    plt.figure()
    plt.plot(history.history['accuracy'], label='Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title(f'Accuracy for {data_file_name}')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    # plt.savefig(f'plot/accuracy_{data_file_name}.pdf', bbox_inches='tight')
    plt.show()

def plot_model_loss(history):
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper right')
    plt.show()



plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
#sourcelink = 'D:/ductri_dataset/'
sourcelink = 'C:/Users/trg14/PycharmProjects/RamanMainProject/ductri_dataset/'

# sourcelink = 'C:/Users/trg14/PycharmProjects/RamanMainProject/ductri_dataset/Ten_labels'

# sourcelink = 'C:/Users/trg14/PycharmProjects/RamanMainProject/ductri_dataset/data'

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directoryimport matplotlib.pyplot as plt
import seaborn as sns

data_file_name = 'earData'
label_file_name = 'target'

# data_file_name = 'Tenlabels_RamanData'
# label_file_name = 'Tenlabels_labels'

data = pd.read_csv(f'{sourcelink}matlab_3/{data_file_name}.csv', header=None)
# data = pd.read_csv(f'{sourcelink}/{data_file_name}.csv', header=None)
data = data.to_numpy()

#target = pd.read_csv(sourcelink + '/' + label_file_name + '.csv')['has_DM2']
target = pd.read_csv(f'{sourcelink}matlab_raman_preprocessed copy/target.csv')['has_DM2']
# target = pd.read_csv(f'{sourcelink}/{label_file_name}.csv')['has_DM2']
target = np.array([int(x) for x in target])

after_shuffle_data, after_shuffle_label, after_shuffle_order = shuffle_data(data, target)
data = np.array(after_shuffle_data)
target = np.array(after_shuffle_label)

sample_size = data.shape[0]         # number of samples in train set
time_steps = data.shape[1]         # number of features in train set
input_dimension = 1                 # each feature is represented by 1 number

data_reshaped = data.reshape(sample_size, time_steps, input_dimension)
print("After reshape train data shape:\n", data_reshaped.shape)
print("1 Sample shape:\n",data_reshaped[0].shape)
print("An example sample:\n", data_reshaped[0])

target_reshaped = target.reshape(target.shape[0],1,1)
# target_reshaped = keras.utils.to_categorical(target)
print("After reshape train target shape:\n", target_reshaped.shape)
print("1 Sample shape:\n", target_reshaped[0].shape)
print("An example sample:\n", target_reshaped[0])

# Commented out IPython magic to ensure Python compatibility.
# %load_ext tensorboard
# Define Tensorboard as a Keras callback
tensorboard = TensorBoard(
  log_dir='.\logs',
  histogram_freq=1,
  write_images=True
)
keras_callbacks = [
  tensorboard
]

# num_folds = 5
# num_folds = 10
loss_function = tf.keras.losses.BinaryCrossentropy()
# loss_function = tf.keras.losses.CategoricalCrossentropy()
optimizer = Adam(learning_rate=1e-4)
# optimizer = Adadelta()
early_stopping = EarlyStopping(monitor='val_loss', patience=150, verbose=0, mode='auto', restore_best_weights=True)
# batch_size = 8
batch_size = 5

# no_epochs = 2000
no_epochs = 100
# verbosity = 0
acc_per_fold = []
loss_per_fold = []


n_timesteps = data_reshaped.shape[1] #10
print(n_timesteps)

n_features = data_reshaped.shape[2] #1
print(n_features)

model = keras.Sequential(name="model_conv1D")
model.add(keras.layers.Input(shape=(n_timesteps, n_features)))
# model.add(keras.layers.Conv1D(filters=200, kernel_size=24, activation='relu', name="Conv1D_1", kernel_regularizer=l2(0.05)))
# model.add(Dropout(0.2))
# model.add(MaxPooling1D(pool_size=2))
model.add(keras.layers.Conv1D(filters=100, kernel_size=12, activation='relu', name="Conv1D_2", kernel_regularizer=l2(0.05)))
model.add(keras.layers.Conv1D(filters=50, kernel_size=6, activation='relu', name="Conv1D_3", kernel_regularizer=l2(0.05)))
model.add(keras.layers.Conv1D(filters=25, kernel_size=3, activation='relu', name="Conv1D_4", kernel_regularizer=l2(0.05)))
# model.add(Dropout(0.2))
# model.add(MaxPooling1D(pool_size=2))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(100, activation='relu', name="Dense_2"))
# model.add(keras.layers.Dense(10, activation='softmax', name="Softmax"))
model.add(keras.layers.Dense(1, activation='sigmoid', name="Sigmoid"))

# Compile the model
model.compile(loss=loss_function,
              optimizer=optimizer,
              metrics=['accuracy'])
model.summary()

# Fit data to model
history = model.fit(data_reshaped, target_reshaped,
            batch_size = batch_size,
            epochs = no_epochs,
            verbose = 1,
            validation_split = 0.2,
            callbacks=keras_callbacks
)

model.evaluate(data_reshaped, target_reshaped)

graph = plt.plot(history.history['accuracy'], label='Accuracy')
accuracy_array = graph[0].get_data()[1]
print("Accuracy", accuracy_array)
turn = 0
sum = 0
for value in accuracy_array:
    # print(value)
    turn = turn + 1
    sum = sum + value
average = sum / turn
print("Average accuracy: ", average)
print("Average accuracy: ", np.mean(history.history['accuracy']))
print("Average validation accuracy: ", np.mean(history.history['val_accuracy']))
plot_history(history)
# cross_val_score(model, earData_reshaped, target_reshaped, cv=RepeatedStratifiedKFold(n_splits=10, random_state=42), scoring='accuracy', n_jobs=-1)
# Commented out IPython magic to ensure Python compatibility.
# %tensorboard --logdir ".\logs" --host localhost --port 8899