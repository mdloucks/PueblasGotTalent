from constants import TRAIN_DIR, TEST_DIR, CSV_DIR
from feature_extraction import stft, spectrogram
from dataloader import load_dataset

from pathlib import Path

from convulutional import ConvulutionalNetwork

import cv2
import numpy as np
# from sklearn.preprocessing import minmax_scale

csv_path = Path(CSV_DIR, 'train.csv')
features, sr, labels = load_dataset(TRAIN_DIR, csv_path, sample_limit=20)

print('generating spectrograms...')
# preprocess
for i in range(len(features)):
    features[i] = spectrogram(features[i], sr[i], max_freq=8e3)
    features[i] = cv2.resize(features[i], (161, 800))

    # features[i] = minmax_scale(features[0], feature_range=(0,1))


model = ConvulutionalNetwork()
model.fit(features, labels, 'output.model')    
