import numpy as np
from scipy.io import wavfile

#######################################################################
#
# ---------------------------------------------------------------------
# Function calculate_dB_level(string)
# ---------------------------------------------------------------------
# This function will take in a string as input and return the
# following:

#       - A float and a string value containing the information of the
#         dB level and vicinity of the sound, respectively.
#
# What determines how this function works is if there is an initial
# dB level defined. The global variable "dB_level" defined at the
# bottom of this file has value float('-inf'); non-existent.
#
# Ex:
# If dB level has no initial value, set it and return values float and
# '' (this empty string indicates that the vicinity cannot be
# determined due to there being no initial dB value to compare to.
#
#######################################################################
def calculate_dB_level(file):

    global dB_level
    global dB_level_2

    if isinstance(file, str):                          # If it is a file path
        sample_rate, audio_data = wavfile.read(file)
    else:                                              # Assuming it's a numpy array
        audio_data = file

    # Check if the there is not an initial dB level
    if dB_level == 0:

        # If so, then set it
        if np.max(np.abs(audio_data)) > 0:
            dB_level = 20 * np.log10(np.max(np.abs(audio_data)))
        else:
            dB_level = 0

        return dB_level, ''

    # Otherwise, start comparisons
    else:

        # If so, then set it and compare only when there is a sound present
        if np.max(np.abs(audio_data)) > 0:
            dB_level_2 = 20 * np.log10(np.max(np.abs(audio_data)))
            compare_dB_levels(dB_level_2)
            dB_level = dB_level_2
        else:
            dB_level = 0

        return dB_level, position_to_sound

#######################################################################
#
# ---------------------------------------------------------------------
# Function compare_dB_levels(float)
# ---------------------------------------------------------------------
# This function will take in a float as input and return a string.
# This string is dependent on a boolean defined through the comparison
# between one dB level to another.
#
# Ex:
# If the current dB level is greater than the previous this function
# will return value "Closer to sound".
#
#######################################################################
def compare_dB_levels(current_dB):

    global position_to_sound

    position_to_sound = 'Closer to the sound' if current_dB > dB_level else 'Further from the sound'


dB_level = 0
dB_level_2 = 0
position_to_sound = ''
