# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# This file will contain relevant feature extraction methods
# such as fourier transforms or MFCC's
# .................................................................
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

from constants import MAX_FREQ, MIN_FREQ


def melspectrogram(y, sr, disp=False):
    sgram = librosa.stft(y)
    sgram_mag, _ = librosa.magphase(sgram)
    mel_scale_sgram = librosa.feature.melspectrogram(S=sgram_mag, sr=sr,
                                                     fmin=MIN_FREQ, fmax=MAX_FREQ)
    mel_sgram = librosa.amplitude_to_db(mel_scale_sgram, ref=np.min)

    if disp:
        librosa.display.specshow(mel_sgram, sr=sr, x_axis='time', y_axis='mel',
                                 fmin=MIN_FREQ, fmax=MAX_FREQ)
        plt.colorbar(format='%+2.0f dB')
        plt.show()

    return mel_sgram
