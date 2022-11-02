
from gc import callbacks
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D, Activation
import tensorflow as tf
from pathlib import PurePath
import matplotlib.pyplot as plt
import numpy as np
import datetime
from constants import MODEL_DIR, IMG_SIZE_X, IMG_SIZE_Y


class ConvulutionalNetwork():

    def __init__(self):

        self.n_epochs = 30

    def fit(self, generator, filename=None):

        model = Sequential()

        input_shape = (IMG_SIZE_X, IMG_SIZE_Y, 1)

        # stack the inputs
        # X = tf.stack(X)
        # y = tf.stack(y)

        model.add(tf.keras.layers.Conv2D(64, (32, 32),
                                         kernel_initializer='he_normal', input_shape=input_shape))
        model.add(tf.keras.layers.BatchNormalization())
        model.add(tf.keras.layers.Activation('relu'))
        model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))

        model.add(tf.keras.layers.Conv2D(
            64, (24, 24), kernel_initializer='he_normal'))
        model.add(tf.keras.layers.BatchNormalization())
        model.add(tf.keras.layers.Activation('relu'))
        model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))

        model.add(tf.keras.layers.Conv2D(
            128, (10, 10), kernel_initializer='he_normal'))
        model.add(tf.keras.layers.BatchNormalization())
        model.add(tf.keras.layers.Activation('relu'))
        model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))

        # this converts our 3D feature maps to 1D feature vectors
        model.add(Flatten())
        model.add(Dense(64, activation=tf.nn.relu))
        model.add(Dropout(0.5))
        model.add(Dense(100, activation=tf.nn.relu))
        model.add(Dropout(0.4))
        model.add(Dense(1))

        optimizer = tf.keras.optimizers.Adam(learning_rate=0.005)

        metric = 'mean_absolute_error'

        model.compile(loss='mean_squared_error',
                      optimizer=optimizer,
                      metrics=[metric])

        callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=5,
                                                    restore_best_weights=True)

        history = model.fit(generator, epochs=self.n_epochs,
                            callbacks=[callback])

        path = PurePath(MODEL_DIR, filename)

        print("saving to", path, "...")
        model.save(path)

        print("finished")

        plt.plot(range(len(history.history[metric])),
                 history.history[metric][:self.n_epochs], color="red")
        plt.xlabel("epochs")
        plt.ylabel(metric)

        plt.show()
