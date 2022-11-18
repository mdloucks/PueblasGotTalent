
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

    def __init__(self, model=None, n_epochs=5, metrics=['mean_absolute_error']):
        """Construct conv network

        Args:
            model (tensorflow.keras.models.Sequential, optional): pretrained model. Defaults to None.
            n_epochs (int, optional): number of epochs. Defaults to 10.
            metrics (list, optional): metrics to use. Defaults to ['mean_absolute_error'].
        """
        self.n_epochs = n_epochs
        self.metrics=metrics

        if model is None:
            self.create_model()
        else:
            self.model = model
            

    def create_model(self):
        self.model = Sequential()

        input_shape = (IMG_SIZE_X, IMG_SIZE_Y, 1)

        self.model.add(tf.keras.layers.Conv2D(64, (5, 5),
                                         kernel_initializer='he_normal', input_shape=input_shape))
        self.model.add(tf.keras.layers.BatchNormalization())
        self.model.add(tf.keras.layers.Activation('relu'))
        self.model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.6))

        self.model.add(tf.keras.layers.Conv2D(
            64, (3, 3), kernel_initializer='he_normal'))
        self.model.add(tf.keras.layers.BatchNormalization())
        self.model.add(tf.keras.layers.Activation('relu'))
        self.model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.6))

        self.model.add(tf.keras.layers.Conv2D(
        32, (2, 2), kernel_initializer='he_normal'))
        self.model.add(tf.keras.layers.BatchNormalization())
        self.model.add(tf.keras.layers.Activation('relu'))
        self.model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.6))

        # this converts our 3D feature maps to 1D feature vectors
        self.model.add(Flatten())
        self.model.add(Dense(64, activation=tf.nn.relu))
        self.model.add(Dropout(0.7))
        self.model.add(Dense(32, activation=tf.nn.relu))
        self.model.add(Dropout(0.4))
        self.model.add(Dense(32, activation=tf.nn.relu))
        self.model.add(Dropout(0.7))
        self.model.add(Dense(1, kernel_initializer='normal'))

        optimizer = tf.keras.optimizers.Adam(learning_rate=0.0005)

        self.model.compile(loss='mse',
                      optimizer=optimizer,
                      metrics=self.metrics)


    def fit(self, generator, filename='out.model'):
        """Fit self.model using the given generator

        Args:
            generator (generator): data generator or list
            filename (str, optional): filename to save to. Defaults to out.model.
        """

        callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3,
                                                    restore_best_weights=True)

        history = self.model.fit(generator, epochs=self.n_epochs,
                            callbacks=[callback])

        path = PurePath(MODEL_DIR, filename)

        print("saving to", path, "...")
        self.model.save(path)

        print("finished")
        
        # plot history of all metrics
        for metric in self.metrics:
            plt.plot(range(len(history.history[metric])),
                    history.history[metric][:self.n_epochs], color="red")
            plt.xlabel("epochs")
            plt.ylabel(metric)

            plt.show()
