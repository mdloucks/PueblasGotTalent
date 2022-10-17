
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D, Activation
from pathlib import PurePath
import matplotlib.pyplot as plt
import numpy as np
import datetime
from constants import MODEL_DIR


class NeuralNetwork():

    def fit(self, X, y, filename):

        model = Sequential()

        model.add(tf.keras.layers.Conv2D(128, (32, 32), kernel_initializer='he_normal', input_shape=X.shape[1:]))
        model.add(tf.keras.layers.BatchNormalization())
        model.add(tf.keras.layers.Activation('relu'))
        model.add(tf.keras.layers.MaxPool2D(pool_size=(3, 3)))

        model.add(tf.keras.layers.Conv2D(128, (24, 24), kernel_initializer='he_normal'))
        model.add(tf.keras.layers.BatchNormalization())
        model.add(tf.keras.layers.Activation('relu'))
        model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))

        model.add(tf.keras.layers.Conv2D(256, (10, 10), kernel_initializer='he_normal'))
        model.add(tf.keras.layers.BatchNormalization())
        model.add(tf.keras.layers.Activation('relu'))
        model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))

        model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
        model.add(Dense(256, activation=tf.nn.relu))
        model.add(Dropout(0.5))
        model.add(Dense(128, activation=tf.nn.relu))
        model.add(Dropout(0.4))
        model.add(Dense(1))

        optimizer = tf.keras.optimizers.Adam(lr=0.001)

        model.compile(loss='mean_squared_error',
                      optimizer=optimizer,
                      metrics=['mean_absolute_error'])

        history = model.fit(X, y, batch_size=16, epochs=self.FLAGS.n_epochs,
                  validation_split=0.2)

        path = PurePath(MODEL_DIR, filename)

        print("saving to", path, "...")
        model.save(path)

        print("finished")

        plt.plot(range(len(history.history["val_loss"])), history.history["val_loss"][:self.FLAGS.n_epochs], color="red")
        plt.xlabel("epochs")
        plt.ylabel("val_loss")
        
        plt.show()