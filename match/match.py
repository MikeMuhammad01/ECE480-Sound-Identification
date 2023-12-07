import math
import os
import librosa
import noisereduce as nr
import numpy as np
from dtw import dtw
from librosa.feature import mfcc

#######################################################################
#
# ---------------------------------------------------------------------
# Function extract_features(string)
# ---------------------------------------------------------------------
# This function will take in a string as input and return a NumPy
# array. In between these operations, the string, which in this case
# is an audio file, will be noise reduced.
#
# The works Mel Frequency Cepstra Coefficients (mfcc) function
# can be better understood through reading the following resources:
#
# --------------------------------Links--------------------------------
# https://en.wikipedia.org/wiki/Mel-frequency_cepstrum
# https://en.wikipedia.org/wiki/Mel_scale
#
# Other links include:
# https://pypi.org/project/noisereduce/#:~:text=Noise%20reduction%20in
# %20python%20using%20spectral%20gating&text=It%20relies%20on%20a%20
# method,band%20of%20that%20signal%2Fnoise.
# --------------------------------Links--------------------------------
#
#######################################################################
def extract_features(file_path):
    audio, fs = librosa.load(file_path)

    if np.isfinite(nr.reduce_noise(y=audio, sr=fs)).all():
        audio = nr.reduce_noise(y=audio, sr=fs)
        return mfcc(y=audio, sr=fs)

    return mfcc(y=audio, sr=fs)

#######################################################################
#
# ---------------------------------------------------------------------
# Function compute_similatiry(np.array, np.array)
# ---------------------------------------------------------------------
# This function will take in two NumPy arrays as input and return a
# string. More specifically, this function will compute the similarity
# between two arrays using dynamic time warping.
#
# Source code for the dtw function as well as information on the
# workings of dynamic time warping can be found here, respectively:
#
# --------------------------------Links--------------------------------
# https://github.com/pollen-robotics/dtw
# https://en.wikipedia.org/wiki/Dynamic_time_warping
# --------------------------------Links--------------------------------
#
#######################################################################
def compute_similarity(features1, features2):
    return dtw(x=features1.T, y=features2.T, dist=math.dist)[0]

#######################################################################
#
# ---------------------------------------------------------------------
# Function match_recording(string)
# ---------------------------------------------------------------------
# This function will take in a string as input and return a string.
# Summarizing this function in more depth, it will iterate over all
# the sounds defined in the 'Sounds' directory of this project
# extracting mfcc's of each sound and comparing with the mfcc of the
# audio recording until the best match is found.
#
#######################################################################
def match_recording(recording_path):
    recording_features = extract_features(recording_path)

    max_difference = float('inf')
    most_similar_file = None

    for file_name in os.listdir(repository_path):

        if file_name.endswith('.wav'):
            file_path = os.path.join(repository_path, file_name)
            file_features = extract_features(file_path)

        difference = compute_similarity(file_features, recording_features)

        if difference < max_difference:
            max_difference = difference
            most_similar_file = file_name

    return most_similar_file

# Repository containing the sounds that will be used to compare the audio
# recording with
repository_path = 'Sounds/'

