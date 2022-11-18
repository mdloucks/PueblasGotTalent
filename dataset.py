# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Helps organize and load the dataset for use by the neural net
# .................................................................

import librosa
from pathlib import Path

import os

import numpy as np


def load_dataset(csv_path: Path, wav_dir: Path, sample_limit=None):
    """
    Loads the dataset of wav filenames as well as labels. This will not load
    any audio data into memory, but is instead to be used as the source for
    the datagenerator.py class. 

    Args:
        csv_path (Path): filepath for csv file

    Yields:
        tuple: x, y tuple with file names and audio labels
    """

    print('loading dataset...')

    with open(csv_path, 'r') as f:
        lines = f.readlines()

    label_keys = ['Head', 'Chest',	'Openess', 'Breathy',
                  'Vibrato', 'Front', 'Back']

    filename_lst: list = []
    labels_lst: list = []

    for i, line in enumerate(lines):

        line = line.split(',')

        # make a column-to-index dict
        if i == 0:
            cols = {col.strip('\n'): j for j, col in enumerate(line)}
            continue

        video_id = line[cols['Link']]
        seg_num = line[cols['seg_num']]
        filename = f"{video_id}-{seg_num}.wav"
        fullpath = Path(os.getcwd(), wav_dir, filename)

        if not (fullpath.exists()):
            continue

        # TODO: experiment using multiple labels
        
        # use sum of all of the columns 
        # labels = sum([float(line[cols[label_key]]) for label_key in label_keys])

        labels = float(line[cols['Openess']])
        
        filename_lst.append(fullpath)
        labels_lst.append(labels)

        print(f'\r{i} out of {len(lines) - 1}...', end='', flush=True)

        if sample_limit:
            if i >= sample_limit:
                break

    print('\ndataset loaded')

    return filename_lst, labels_lst

# def load_dataset(wav_dir: Path, csv_path: Path, sample_limit=None):
#     """loads the dataset using librosa by loading the raw wav data. This
#     can then be converted into other formats as desired.


#     Args:
#         wav_dir (Path): directory containing wav files
#         csv_path (Path): filepath for csv file

#     Yields:
#         tuple: x, y tuple with raw file data and audio labels
#     """

#     print('loading dataset...')

#     with open(csv_path, 'r') as f:
#         lines = f.readlines()

#     label_keys = ['Head', 'Chest',	'Openess', 'Breathy',
#                    'Vibrato', 'Front', 'Back']

#     y_lst = []
#     sr_lst = []
#     labels_lst = []

#     for i, line in enumerate(lines):
#         line = line.split(',')

#         # make a column-to-index dict
#         if i == 0:
#             cols = {col.strip('\n'): j for j, col in enumerate(line)}
#             continue


#         video_id = line[cols['Link']]
#         seg_num = line[cols['seg_num']]
#         filename = f"{video_id}-{seg_num}.wav"
#         fullpath = Path(os.getcwd(), wav_dir, filename)

#         labels = np.array([float(line[cols[label_key]]) for label_key in label_keys], dtype=np.float32)

#         if not (fullpath.exists()):
#             continue

#         print(f'\r{i} out of {len(lines) - 1}...', end='', flush=True)

#         try:
#             y, sr = librosa.load(fullpath, mono=True)
#             # problem with audio file
#         except ValueError:
#             continue

#         y_lst.append(y)
#         sr_lst.append(sr)
#         labels_lst.append(labels)

#         if sample_limit:
#             if i >= sample_limit:
#                 break


#     print('\ndataset loaded')

#         # y_lst = np.array(y_lst, dtype=np.float32),
#         # sr_lst = np.array(sr_lst, dtype=np.float32),
#         # labels_lst = np.array(labels_lst, np.float32)

#     return y_lst, sr_lst, labels_lst
