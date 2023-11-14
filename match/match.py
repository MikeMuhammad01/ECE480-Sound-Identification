import math
import statistics
import os

import librosa
import numpy
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
    recording_features = numpy.split(extract_features(recording_path),
                                     len(extract_features(recording_path))//2)

    max_difference = float('inf')
    most_similar_file = None

    for file_name in os.listdir(repository_path):

        difference = []

        if file_name.endswith('.wav'):
            file_path = os.path.join(repository_path, file_name)
            file_features = numpy.split(extract_features(file_path),
                                        len(extract_features(file_path)) // 2)

            for i in range(0, len(recording_features)):
                difference.append(compute_similarity(recording_features[i], file_features[i]))

        avg_distance = statistics.mean(difference)

        if avg_distance < max_difference:
            max_difference = avg_distance
            most_similar_file = file_name

    return most_similar_file

repository_path = 'Sounds/'

