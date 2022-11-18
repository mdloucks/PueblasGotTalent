import keras
import numpy as np

from pathlib import Path

from feature_extraction import melspectrogram

import librosa

from constants import IMG_SIZE_X, IMG_SIZE_Y

from keras import backend as K

from sklearn.preprocessing import StandardScaler


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Used to generate the spectrograms from raw wav files
#.................................................................  
class SpectrogramGenerator(keras.utils.Sequence):
    def __init__(self, data_filenames, labels, batch_size, image_size):
        self.data_filenames = data_filenames
        self.labels = labels
        self.batch_size = batch_size
        self.image_size = image_size
        self.work_dir = Path(".").parent.absolute()
        self.num_classes = 4
        self.shuffle = True


    def __len__(self):
        return (np.ceil(len(self.data_filenames) / self.batch_size)).astype(np.int)

    def __getitem__(self, idx):
        # this is the slice of items for the given batch
        data_batch = self.data_filenames[idx * self.batch_size : (idx+1) * self.batch_size]
        data_labels_batch = self.labels[idx * self.batch_size : (idx+1) * self.batch_size]

        batch_spectrograms: list = []
        batch_labels: list = []

        for filename, label in list(zip(data_batch, data_labels_batch)):
            try:
                y, sr = librosa.load(filename)
            # there's something wrong with the audio file, skip
            except ValueError:
                continue

            spectrogram = self._preprocess_audio(y, sr)

            # standardize
            scaler = StandardScaler()
            scaler.fit(spectrogram)
            spectrogram = scaler.transform(spectrogram)

            # one-hot our labels for categorization
            # label = K.one_hot(K.cast(label, 'uint8'),
            #               num_classes=self.num_classes)

            batch_spectrograms.append(spectrogram)
            batch_labels.append(label)

        return np.array(batch_spectrograms), np.array(batch_labels)

    def _preprocess_audio(self, y, sr):
        mel_sgram = melspectrogram(y, sr)

        # too small, pad with zeros
        if mel_sgram.shape[1] < IMG_SIZE_Y:
            pad_amount = IMG_SIZE_Y - mel_sgram.shape[1]
            mel_sgram = np.pad(mel_sgram, ((0,0),(0,pad_amount)), 'constant')
        # too big, truncate
        elif mel_sgram.shape[1] > IMG_SIZE_Y:
            mel_sgram = mel_sgram[:, :IMG_SIZE_Y]


        return mel_sgram


