import os
import numpy as np
import sounddevice as sd
from scipy.io import wavfile
from scipy.spatial.distance import cdist
from python_speech_features import mfcc

def extract_features(file_path):
    sample_rate, audio = wavfile.read(file_path)
    features = mfcc(audio, sample_rate)
    print(features)
    return features

def compute_similarity(features1, features2):
    distance_matrix = cdist(features1, features2, metric='euclidean')
    similarity = np.mean(distance_matrix)
    return similarity

def match_recording(recording_path, folder_path):
    recording_features = extract_features(recording_path)
    max_similarity = float('inf')
    most_similar_file = None

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.wav'):
            file_path = os.path.join(folder_path, file_name)
            file_features = extract_features(file_path)
            similarity = compute_similarity(recording_features, file_features)

            if similarity < max_similarity:
                max_similarity = similarity
                most_similar_file = file_name

    return most_similar_file

def record_audio(file_path, duration):
    fs = 44100  
    print("recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    wavfile.write(file_path, fs, audio)


recording_duration = 5


recording_file_path = 'recording.wav'


folder_path = '\Sounds'


record_audio(recording_file_path, recording_duration)


most_similar_file = match_recording(recording_file_path, folder_path)
print('most similar wav:', most_similar_file)
