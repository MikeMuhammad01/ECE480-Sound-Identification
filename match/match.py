import math
import os

import librosa
import noisereduce as nr

from dtw import dtw
from librosa.feature import mfcc


def extract_features(file_path):
    audio, fs = librosa.load(file_path)
    audio = nr.reduce_noise(y=audio, sr=fs)
    return mfcc(y=audio, sr=fs)


def compute_similarity(features1, features2):
    return dtw(x=features1.T, y=features2.T, dist=math.dist)[0]


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

repository_path = 'Sounds/'

