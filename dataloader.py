# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Helps organize and load the dataset for use by the neural net
# .................................................................

import librosa
from pathlib import Path
from constants import TRAIN_DIR, TEST_DIR, CSV_DIR

import os


def load_dataset(wav_dir: Path, csv_path: Path):
    """loads the dataset using librosa by loading the raw wav data. This
    can then be converted into other formats as desired.

    Args:
        wav_dir (Path): directory containing wav files
        csv_path (Path): filepath for csv file

    Yields:
        tuple: x, y tuple with raw file data and audio labels
    """

    with open(csv_path, 'r') as f:
        lines = f.readlines()

    label_keys = ['Head', 'Chest',	'Openess', 'Breathy',
                   'Vibrato', 'Front', 'Back']

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

        labels = [line[cols[label_key]] for label_key in label_keys]
        print(labels)

        if not (fullpath.exists()):
            continue

        file = load_file(fullpath)
        
        yield file, labels


def load_file(filepath: Path):
    """load the given file using librosa

    Args:
        filepath (Path): filepath

    Returns:
        np.array: np array containing audio data.
    """
    if not (filepath.exists()):
        return False

    file = librosa.load(filepath, mono=True)

    return file


csv_path = Path(CSV_DIR, 'train.csv')
data = load_dataset(TRAIN_DIR, csv_path)

for d in data:
    print(d)
    break
