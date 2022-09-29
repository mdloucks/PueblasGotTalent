# a script that will take the video links found in the csv files and
# download them to a given directory

from io import TextIOWrapper
import os
import glob
from pytube import YouTube
import pytube
import urllib

from preprocessing.constants import CSV_DIR, TEST_DIR_RAW, TRAIN_DIR_RAW

def download_csv(csv_path, output_dir):
    """Download the videos of the given csv file to the given download folder

    Args:
        csv_name (str): csv path
        download_folder (str): folder path
    """

    blacklist_fp: TextIOWrapper = open('preprocessing/blacklist.txt', 'r')
    blacklist_dict = {line.strip(): 0 for line in blacklist_fp.readlines()}

    with open(csv_path, 'r') as f:

        lines = f.readlines()

        for i, line in enumerate(lines):

            line = line.split(',')

            # make a column-to-index dict
            if i == 0:
                cols = {col: j for j, col in enumerate(line)}
                continue

            video_id = line[cols['Link']]

            # skip if blacklisted
            if video_id in blacklist_dict:
                continue

            # check to see if the download path exists with any extension
            download_path = os.path.join(output_dir,
                                             f"{video_id}")

            if glob.glob(f'{download_path}.*'):
                continue

            print(f'\rDownloading {download_path}: {i} out of {len(lines)}...', end='',
                                                             flush=True)

            # try to download, if not add to blacklist
            if not(download_video(video_id, output_dir)):
                add_to_blacklist(line[cols['Link']])

            
def add_to_blacklist(video_id):
    """Add the given video_id to the blacklist

    Args:
        link (str): Youtube link
    """
    blacklist_fp: TextIOWrapper = open('blacklist.txt', 'a')
    blacklist_fp.write(video_id + '\n')


def download_video(video_id: str, output_dir: str):
    """Download the given youtube URL to the given output with the
    link ID being used as the filename and given the default extension

    Args:
        video_id (str): youtube video_id
        output_dir (str): output path
    """

    link = f"https://www.youtube.com/watch?v={video_id}"

    try:
        yt = YouTube(link)
        ys = yt.streams.get_audio_only()
        ys.download(output_path=output_dir, filename=f'{video_id}.{ys.subtype}')
        return True
        # if the audio doesn't exist, download the video
    except urllib.error.HTTPError as e:
        return False
    except pytube.exceptions.VideoUnavailable as e:
        return False
    except OSError:
        return False
    except KeyboardInterrupt:
        raise Exception('keyboard interrupt')
        



if __name__ == '__main__':
    download_csv(os.path.join(CSV_DIR, 'test.csv'), TEST_DIR_RAW)
    download_csv(os.path.join(CSV_DIR, 'train.csv'), TRAIN_DIR_RAW)