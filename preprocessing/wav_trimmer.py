# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Trim down all of the wav files to their desired size
# .................................................................

from ctypes import Union
import os
import time

from constants import TEST_DIR_RAW, TRAIN_DIR_RAW, CSV_DIR
from constants import TEST_DIR_WAV, TRAIN_DIR_WAV

from pathlib import Path

import re

def trim_wav(file_path: str, start: float, end: float):
    """trim the wav of a given file path

    Args:
        file_path (str): file path
        start (float): start timestamp
        end (float): end timestamp
    """


def trim_dir(input_dir: str, del_originals = True):
    """Trim all of the files within a given directory using the csv specified
    in constants.py

    In addition this function will also purge all of the original wav files 
    that it converts in order to converve space. 

    Args:
        input_dir (str): directory to trim
    """

    with open(os.path.join(CSV_DIR, 'seg_time_lists.csv'), 'r') as f:
        lines = f.readlines()

    cols = {}

    for i, line in enumerate(lines):

        line = line.split(',')

        # make a column-to-index dict
        if i == 0:
            cols = {col.strip('\n'): j for j, col in enumerate(line)}
            continue

        filename = f"{line[cols['name']]}.wav"
        seg_num = line[cols['num']]
        start = float(line[cols['time_start']])
        end = float(line[cols['time_end']])
        filepath = os.path.join(input_dir, filename)

        print(f'\r{i} out of {len(lines) - 1}...', end='', flush=True)

        trim_wav(filepath, seg_num, start, end)


    if del_originals:
        print('deleting originals...')
        del_wavs(input_dir)


def trim_wav(filepath: str, seg_num: int, start: float, end: float):
    """Trim a given wav to the specified length in seconds

    Args:
        filepath (str): filepath for wav
        seg_num (int): segment number
        start (float): start time in seconds
        end (float): end time in seconds
    """

    if not (os.path.isfile(filepath)):
        return

    duration = end - start

    # output filename with segment number
    output_file = f"{filepath[:-4]}-{seg_num}.wav"

    command = f'ffmpeg -y -i {filepath} -ss {start} -t {duration} -c:v copy \
                -c:a copy {output_file} -loglevel error'

    os.system(command)


def del_wavs(input_dir: str):
    
    for filename in os.listdir(input_dir):

        pattern = r"(-[0-9]{1,2}.wav)$"
        if len(re.findall(pattern, filename)) == 0:
            full_path = os.path.join(os.getcwd(), input_dir, filename)
            command = f'rm {full_path}'

            os.system(command)

if __name__ == '__main__':
    trim_dir(TRAIN_DIR_WAV)
    trim_dir(TEST_DIR_WAV)
