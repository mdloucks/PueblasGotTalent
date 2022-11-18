from constants import TRAIN_DIR, TEST_DIR, CSV_DIR, IMG_SIZE_X, IMG_SIZE_Y

from dataset import load_dataset
from datagenerator import SpectrogramGenerator

from pathlib import Path

from convulutional import ConvulutionalNetwork

import cv2
import numpy as np

import tensorflow as tf

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Script to run for training the network.
#.................................................................

continue_training = True
model_name = 'output_openness.model'

csv_path = Path(CSV_DIR, 'train.csv')
filenames_lst, labels_lst = load_dataset(csv_path, TRAIN_DIR, sample_limit=None)

print('generating spectrograms...')
spec_gen = SpectrogramGenerator(filenames_lst, labels_lst,
                                16, (IMG_SIZE_X, IMG_SIZE_Y))

# continue training previous model
if continue_training:
    print('continuing previous training...')
    
    model = tf.keras.models.load_model('models/' + model_name)
    model = ConvulutionalNetwork(model)
    model.fit(spec_gen, 'output_head.model')

    pass
# start from scratch
else:
    print('training from scratch...')

    model = ConvulutionalNetwork()
    model.fit(spec_gen, model_name)
