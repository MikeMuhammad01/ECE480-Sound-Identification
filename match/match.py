import math
import os

import librosa
import sounddevice as sd

from dtw import dtw
from librosa.feature import mfcc
from scipy.io import wavfile


def extract_features(file_path):
    audio, fs = librosa.load(file_path)
    return mfcc(y=audio, sr=fs)


def compute_similarity(features1, features2):
    return dtw(x=features1.T, y=features2.T, dist=math.dist)[0]


def match_recording(recording_path):
    recording_features = extract_features(recording_path)
    max_similarity = float('inf')
    most_similar_file = None

    for file_name in os.listdir(repository_path):
        if file_name.endswith('.wav'):
            file_path = os.path.join(repository_path, file_name)
            file_features = extract_features(file_path)
            similarity = compute_similarity(recording_features, file_features)

            if similarity < max_similarity:
                max_similarity = similarity
                most_similar_file = file_name.replace('.wav', '')

    return most_similar_file


def record_audio(file_path, duration):
    fs = 44100  
    print("recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    wavfile.write(file_path, fs, audio)


recording_duration = 5
recording_file_path = 'recording.wav'
repository_path = 'Sounds/'

