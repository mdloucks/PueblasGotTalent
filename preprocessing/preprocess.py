from dataset_downloader import download_csv
from wav_converter import convert_to_wav
from wav_trimmer import trim_dir

from constants import TEST_DIR_RAW, TRAIN_DIR_RAW, CSV_DIR
from constants import TEST_DIR_WAV, TRAIN_DIR_WAV

import os


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# This file links together all of the processes in the other files
# in one easy-to-use preprocessing step
#.................................................................

def preprocess():
    print("Downloading mp4 data...")
    download_csv(os.path.join(CSV_DIR, 'test.csv'), TEST_DIR_RAW)
    download_csv(os.path.join(CSV_DIR, 'train.csv'), TRAIN_DIR_RAW)

    print("Converting to wav...")
    convert_to_wav(TEST_DIR_RAW, TEST_DIR_WAV)
    convert_to_wav(TRAIN_DIR_RAW, TRAIN_DIR_WAV)

    print("Trimming audio...")
    trim_dir(TRAIN_DIR_WAV)
    trim_dir(TEST_DIR_WAV)

    print()
    print("Operations completed.")
    

if __name__ == '__main__':
    preprocess()