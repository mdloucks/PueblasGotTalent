# a script that will take the video links found in the csv files and 
# download them to a given directory

import pafy
import os

def download_csv(csv_path, download_dir):
    """Download the videos of the given csv file to the given download folder


    Args:
        csv_name (str): csv path
        download_folder (str): folder path
    """

    with open(csv_path, 'r') as f:
        for i, line in enumerate(f.readlines()):

            line = line.split(',')

            # make a column-to-index dict
            if i == 0:
                cols = {col: j for j, col in enumerate(line)}
                continue

            # see if file exists first
            download_path = os.path.join(download_dir,
                                        f"{line[cols['Link']]}.mp4")

            if(os.path.exists(download_path)):
                continue

            try:
                video = pafy.new(
                            f"https://www.youtube.com/watch?v={line[cols['Link']]}")

                print(f'\rDownloading {video.title}...', flush=True, end='')

                best = video.getbest(preftype ="mp4")
    
                best.download(download_path)
                # ignore any missing videos
            except Exception as e:
                continue
            return



if __name__ == '__main__':
    download_csv('./train.csv', '../audio/SVQTD/')