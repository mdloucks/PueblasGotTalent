from constants import TRAIN_DIR, TEST_DIR, CSV_DIR, IMG_SIZE_X, IMG_SIZE_Y

from dataset import load_dataset
from datagenerator import SpectrogramGenerator

from pathlib import Path

from convulutional import ConvulutionalNetwork

import cv2
import numpy as np


# from sklearn.preprocessing import minmax_scale

csv_path = Path(CSV_DIR, 'train.csv')
filenames_lst, labels_lst = load_dataset(csv_path, TRAIN_DIR, sample_limit=None)

print('generating spectrograms...')
spec_gen = SpectrogramGenerator(filenames_lst, labels_lst,
                                16, (IMG_SIZE_X, IMG_SIZE_Y))

# spec_gen.__getitem__(0)

model = ConvulutionalNetwork()
model.fit(spec_gen, 'output.model')
# preprocess
# for i in range(len(features)):
#     melspectrogram(features[i], sr[i])
#     # features[i] = spectrogram(features[i], sr[i], max_freq=8e3)
#     # features[i] = cv2.resize(features[i], (161, 800))

#     # features[i] = minmax_scale(features[0], feature_range=(0,1))


