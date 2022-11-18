from constants import TRAIN_DIR, TEST_DIR, CSV_DIR, IMG_SIZE_X, IMG_SIZE_Y

from dataset import load_dataset
from datagenerator import SpectrogramGenerator

from pathlib import Path

from convulutional import ConvulutionalNetwork

import cv2
import numpy as np

import tensorflow as tf

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# This file will generate run inference on our model using the first n samples
# from our test directory. The entire dataset can be used as testing by setting
# the sample limit to None
# ............................................................................................

model = tf.keras.models.load_model('models/output_openness.model')

csv_path = Path(CSV_DIR, 'test.csv')

filenames_lst, labels_lst = load_dataset(csv_path, TEST_DIR, sample_limit=10)

print('generating spectrograms...')
spec_gen = SpectrogramGenerator(filenames_lst, labels_lst,
                                16, (IMG_SIZE_X, IMG_SIZE_Y))

# print(batch)
predictions = model.predict(spec_gen)

total_error = 0

print('\n\n')
print(f"{'file' : <20}{'prediction' : ^10}{'label' : >10}{'error' : >10}")
print(f"{'-'*50}")

for file, pred, label in list(zip(filenames_lst, predictions, labels_lst)):
    error = -round((label - pred[0]) / pred[0], 2)
    total_error += abs(error)
    print(f"{file.stem : <20}{str(pred[0]) : ^10}{str(label) : ^10}{str(100 * error) : >10}%")

print(f"{'-'*50}")
print(f"AVERAGE TEST ERROR: {(total_error * 100) / len(filenames_lst):0.2f}%")
