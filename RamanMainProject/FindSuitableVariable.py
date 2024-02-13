import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import tensorflow as tf
import keras_tuner as kt
from keras.regularizers import l2
from keras_tuner.tuners import RandomSearch
from tensorflow import keras


def build_model(hp):
    model = keras.Sequential(name="model_conv1D")

    # Add layers to the model using the hyperparameters
    model.add(keras.layers.Conv1D(filters=250, kernel_size=24, activation='relu', name="Conv1D_1",kernel_regularizer=l2(0.05)))
    model.add(keras.layers.Conv1D(filters=100, kernel_size=12, activation='relu', name="Conv1D_2",kernel_regularizer=l2(0.05)))
    model.add(keras.layers.Conv1D(filters=50, kernel_size=6, activation='relu', name="Conv1D_3", kernel_regularizer=l2(0.05)))
    model.add(keras.layers.Conv1D(filters=25, kernel_size=3, activation='relu', name="Conv1D_4", kernel_regularizer=l2(0.05)))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(100, activation='relu', name="Dense_2"))
    model.add(keras.layers.Dense(10, activation='Softmax', name="Softmax"))

    # Compile the model
    model.compile(optimizer='adam',
                  loss='CategoricalCrossentropy',
                  metrics=['accuracy'])

    return model

tuner = RandomSearch(
    build_model,
    objective='val_accuracy',
    max_trials=5,
    directory='my_dir',
    project_name='cnn_hyperparameter_tuning'
)

sourcelink = 'C:/Users/trg14/PycharmProjects/RamanMainProject/ductri_dataset/'

data_file_name = 'Tenlabels_RamanData'
label_file_name = 'Tenlabels_labels'

data = pd.read_csv(f'{sourcelink}Ten_labels/{data_file_name}.csv', header=None)
data = data.to_numpy()

target = pd.read_csv(sourcelink + 'Ten_labels/' + label_file_name + '.csv')['has_DM2']
target = np.array([int(x) for x in target])
tuner = kt.Hyperband(build_model,
                     objective='val_accuracy',
                     max_epochs=10,
                     factor=3,
                     directory='my_dir',
                     project_name='intro_to_kt')
stop_early = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=150, verbose=0, mode='auto', restore_best_weights=True)
tuner.search(data, target, epochs=50, validation_split=0.2, callbacks=[stop_early])
best_hps=tuner.get_best_hyperparameters(num_trials=1)[0]
print(f"""
The hyperparameter search is complete. The optimal number of units in the first densely-connected
layer is {best_hps.get('units')} and the optimal learning rate for the optimizer
is {best_hps.get('learning_rate')}.
""")


# conv1_filters = best_hps.get('Conv1D_1')
# conv2_filters = best_hps.get('Conv1D_2')
# conv3_filters = best_hps.get('Conv1D_3')
# conv4_filters = best_hps.get('Conv1D_4')
# dense1_units = best_hps.get('Dense_2')
# dense2_units = best_hps.get('Softmax')
#
# print(f"Best Hyperparameters:")
# print(f"conv1_filters: {conv1_filters}")
# print(f"conv2_filters: {conv2_filters}")
# print(f"conv1_filters: {conv3_filters}")
# print(f"conv2_filters: {conv4_filters}")
# print(f"dense_units: {dense1_units}")
# print(f"dense_units: {dense2_units}")


