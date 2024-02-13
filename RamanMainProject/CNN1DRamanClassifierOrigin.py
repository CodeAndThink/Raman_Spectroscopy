import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from keras.callbacks import EarlyStopping
from keras.callbacks import TensorBoard
from keras.optimizers import Adam
from keras.regularizers import l2
from keras.layers import Dense, Input, Conv1D, Flatten
from keras.models import load_model
import random
from sklearn.metrics import classification_report

def plot_history(history):
    plt.figure()
    plt.plot(history.history['loss'], label='Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title(f'Loss for {data_file_name}')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()

    plt.figure()
    plt.plot(history.history['accuracy'], label='Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title(f'Accuracy for {data_file_name}')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()

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

# Get datas from files
sourcelink = 'Ten_labels'
data_file_name = 'Tenlabels_RamanData'
label_file_name = 'Tenlabels_labels'

data = pd.read_csv(sourcelink + '/' + data_file_name + '.csv', header=None)
data = data.to_numpy()
target = pd.read_csv(sourcelink + '/' + label_file_name + '.csv')['has_DM2']
target = np.array([int(x) for x in target])

# Change order of datas
after_shuffle_data, after_shuffle_label, after_shuffle_order = shuffle_data(data, target)
data = np.array(after_shuffle_data)
target = np.array(after_shuffle_label)

#Define sample_size and time_steps
sample_size = data.shape[0]         # number of samples in train set
time_steps = data.shape[1]         # number of features in train set
input_dimension = 1                 # each feature is represented by 1 number

#Reshape datas
data_reshaped = data.reshape(sample_size, time_steps, input_dimension)
print("After reshape train data shape:\n", data_reshaped.shape)
print("1 Sample shape:\n",data_reshaped[0].shape)
print("An example sample:\n", data_reshaped[0])

target_reshaped = keras.utils.to_categorical(target)
print("After reshape train target shape:\n", target_reshaped.shape)
print("1 Sample shape:\n", target_reshaped[0].shape)
print("An example sample:\n", target_reshaped[0])

#Define tensorboard
tensorboard = TensorBoard(
  log_dir='.\logs',
  histogram_freq=1,
  write_images=True
)

loss_function = tf.keras.losses.CategoricalCrossentropy()
optimizer = Adam(learning_rate=1e-4)
early_stopping = EarlyStopping(monitor='val_loss', patience=50, verbose=1, mode='auto', restore_best_weights=True)
batch_size = 5
no_epochs = 200

keras_callbacks = [
  tensorboard, early_stopping
]

n_timesteps = data_reshaped.shape[1] #10
print(n_timesteps)

n_features = data_reshaped.shape[2] #1
print(n_features)

# Model layers
model = keras.Sequential(name="model_conv1D")
model.add(Input(shape=(n_timesteps, n_features)))
model.add(Conv1D(filters=200, kernel_size=24, activation='relu', name="Conv1D_1", kernel_regularizer=l2(0.05)))
model.add(Conv1D(filters=50, kernel_size=6, activation='relu', name="Conv1D_3", kernel_regularizer=l2(0.05)))
model.add(Conv1D(filters=25, kernel_size=3, activation='relu', name="Conv1D_4", kernel_regularizer=l2(0.05)))
model.add(Flatten())
model.add(Dense(100, activation='relu', name="Dense_1"))
model.add(Dense(50, activation='relu', name="Dense_2"))
model.add(Dense(10, activation='Softmax', name="Softmax"))

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
            callbacks=[keras_callbacks, early_stopping])

model.evaluate(data_reshaped, target_reshaped)

print("Average accuracy: ", np.mean(history.history['accuracy']))
print("Average validation accuracy: ", np.mean(history.history['val_accuracy']))

# Lưu mô hình
model.save('Ten_labels/Save_model/model.h5')

# Load mô hình
# loaded_model = load_model('Ten_labels/Save_model/model.h5')

# plot_history(history)

plt.show()
# tensorboard --logdir C:/Users/trg14/PycharmProjects/RamanMainProject/logs