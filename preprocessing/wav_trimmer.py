#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Trim down all of the wav files to their desired size
#.................................................................

import os

from preprocessing.constants import TEST_DIR_RAW, TRAIN_DIR_RAW, CSV_DIR
from preprocessing.constants import TEST_DIR_WAV, TRAIN_DIR_WAV

command = 'ffmpeg -i l3uij4CF9H8.wav -ss 00:00:00 -t 00:00:10 -c:v copy -c:a copy output1.wav'

def trim_wav(file_path: str, start: float, end: float):
    """trim the wav of a given file path

    Args:
        file_path (str): file path
        start (float): start timestamp
        end (float): end timestamp
    """


def trim_dir(input_dir: str):
    """Trim all of the files within a given directory using the csv specified
    in constants.py

    Args:
        input_dir (str): directory to trim
    """

    with open(os.path.join(CSV_DIR, 'seg_time_lists.csv'), 'r') as f:

        lines = f.readlines()

        for i, line in enumerate(lines):
            print(f'\r{i} out of {len(lines) - 1}...', end='', flush=True)

            filename_root = os.path.splitext(filename)[0]
            filename_wav = f"{filename_root}.wav"
