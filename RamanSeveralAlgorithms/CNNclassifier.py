from keras import Input
from keras.callbacks import EarlyStopping
from keras.layers import Conv1D
from keras.optimizers import Adam
from keras.regularizers import l2

import CSVCSVReader
import FolderLister
import LabelGetter
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn import metrics

# Larger CNN for the MNIST Dataset
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.utils import to_categorical

def loaddata(source_link, folder_name):
    X = []
    y = []
    listfile = FolderLister.listfile(source_link, folder_name)

    labels = LabelGetter.getLabel(listfile)
    for i in range(0, len(listfile)):

        if (labels[i] == '05M'):
            y.append(1)
        else:
            if (labels[i] == '10mM'):
                y.append(2)
            else:
                if (labels[i] == '20mM'):
                    y.append(3)
                else:
                    if (labels[i] == '75M'):
                        y.append(4)
                    else:
                        if (labels[i] == '125M'):
                            y.append(5)
                        else:
                            if (labels[i] == '150M'):
                                y.append(6)
                            else:
                                y.append(0)

        data_array = CSVCSVReader.get_intensity_data(source_link + folder_name + '/', listfile[i])
        X.insert(i, data_array)

    return X, y

# define the larger model
def larger_model():
    # create model
    model = Sequential()
    model.add(Conv2D(30, (5, 5), input_shape=(28, 28, 1), activation='relu'))
    model.add(MaxPooling2D())
    model.add(Conv2D(15, (3, 3), activation='relu'))
    model.add(MaxPooling2D())
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(6, activation='softmax'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def normal_model():
    loss_function = tf.keras.losses.CategoricalCrossentropy()
    optimizer = Adam(learning_rate=1e-4)
    early_stopping = EarlyStopping(monitor='val_loss', patience=150, verbose=0, mode='auto', restore_best_weights=True)

    model = Sequential(name="model_conv1D")
    model.add(Input(shape=(2, 2030)))
    model.add(Conv1D(filters=100, kernel_size=2, activation='relu', name="Conv1D_1", kernel_regularizer=l2(0.05)))
    # model.add(Dropout(0.2))
    # model.add(MaxPooling1D(pool_size=2))
    model.add(Conv1D(filters=50, kernel_size=1, activation='relu', name="Conv1D_2", kernel_regularizer=l2(0.05)))
    # model.add(Dropout(0.2))
    # model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(5, activation='relu', name="Dense_2"))
    model.add(Dense(1, activation='sigmoid', name="Sigmoid"))

    # Compile the model
    model.compile(loss=loss_function, optimizer=optimizer, metrics=['accuracy'])

    model.summary()
    return model

def main():

    training_folder_name = 'training set'
    test_folder_name = 'test set'
    source_link = 'D:/CÔNG VIỆC/TIẾN SĨ/CÔNG VIỆC/2023 - 03 Áp dụng hotpot series extraction vào đoán đường huyết bằng Raman/Mau du lieu/Method 3/'

    X_train = []
    y_train = []
    X_test = []
    y_test = []

    X_train, y_train = loaddata(source_link, training_folder_name)
    X_test, y_test = loaddata(source_link, test_folder_name)

    # y_train = to_categorical(y_train)
    # y_test = to_categorical(y_test)
    # num_classes = y_test.shape[1]

    # print(f"X_train: {X_train}")
    # print(f"y_train: {y_train}")
    # print(f"num_class: {num_classes}")

    # print(len(X_train))
    # print(len(X_train[0]))
    # print(y_train)
    #
    # print(len(X_test))
    # print(len(X_test[0]))
    # print(y_test)

    # build the model
    model = normal_model()
    # Fit the model


    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=2)
    # Final evaluation of the model
    scores = model.evaluate(X_test, y_test, verbose=0)
    print("Large CNN Error: %.2f%%" % (100 - scores[1] * 100))

main()