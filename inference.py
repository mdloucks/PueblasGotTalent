import tensorflow as tf
from dataloader import load_dataset
from constants import TRAIN_DIR, TEST_DIR, CSV_DIR
from pathlib import Path
from feature_extraction import stft, spectrogram
import cv2

model = tf.keras.models.load_model('models/output.model')

csv_path = Path(CSV_DIR, 'test.csv')

features, sr, labels = load_dataset(TEST_DIR, csv_path, sample_limit=1)

# preprocess
for i in range(len(features)):
    features[i] = spectrogram(features[i], sr[i], max_freq=8e3)
    features[i] = cv2.resize(features[i], (161, 800))


# reshape
features[0] = features[0].reshape(-1, 800, 161, 1)

# run
prediction = model.predict(features[0])

print(prediction)