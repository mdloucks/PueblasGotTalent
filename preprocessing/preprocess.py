from dataset_downloader import download_csv


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# This file links together all of the processes in the other files
# in one easy-to-use preprocessing step
#.................................................................


def preprocess():
    download_csv('SVQTD/test.csv', 'audio/SVQTD/test/raw/')
    

if __name__ == '__main__':
    preprocess()