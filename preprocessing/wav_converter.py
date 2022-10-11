# convert the given mp4 files to wav (requires ffmpeg command) and trim them
# this probably won't work on windows

import os
import glob

from constants import TEST_DIR_RAW, TRAIN_DIR_RAW
from constants import TEST_DIR_WAV, TRAIN_DIR_WAV

def convert_to_wav(input_dir, output_dir):
    """Convert all mp4 files in a given directory to wav in a different
    directory

    Args:
        input_dir (str): input dir path
        output_dir (str): output dir path
    """

    input_dir_list: list = os.listdir(input_dir)

    for i, filename in enumerate(input_dir_list):

        print(f'\r{input_dir} to {output_dir}: {i} out of {len(input_dir_list)}...', end='', flush=True)

        filename_root = os.path.splitext(filename)[0]
        filename_wav = f"{filename_root}.wav"

        command = f'ffmpeg -y -i {os.path.join(input_dir, filename)} \
                    {os.path.join(output_dir, filename_wav)} \
                    -loglevel error'

        # execute command (omiting messages)
        os.system(command)



if __name__ == '__main__':
    convert_to_wav(TEST_DIR_RAW, TEST_DIR_WAV)
    convert_to_wav(TRAIN_DIR_RAW, TRAIN_DIR_WAV)