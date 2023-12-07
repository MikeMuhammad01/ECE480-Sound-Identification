import match
import doppler_effect
from flask import Flask, render_template, request

# Create the Flask Application
app = Flask(__name__)

#######################################################################
#
# ---------------------------------------------------------------------
# MODULE 1 - Index.HTML Rendering
# ---------------------------------------------------------------------
# This function will handle the rendering of the JS-based HTML
# document defined as "index.html" in the "templates" directory of
# this project.
#
#######################################################################
@app.route('/')
def index():
    return render_template('index.html')

#######################################################################
#
# ---------------------------------------------------------------------
# MODULE 2 - API Setup
# ---------------------------------------------------------------------
# This function will handle the setup of the sound identification API.
# It will request access to the recorded audio file, process it via
# two main algorithms, and use API method 'POST' to post the results
# to the HTML file for display on the website:
#
#       - match_recording: Match the recording to a sound defined in
#                          the "Sounds" directory this project.
#
#       - calculate_dB_level: Calculate the decibel (dB) level of the
#                             recording.
#
#######################################################################
@app.route('/api/analyze-audio', methods=['POST'])
def analyze_audio():
    file = request.files.get("audio")
    temp_file = 'temp.wav'

    if file:
        file.save(temp_file)
        match_result = match.match_recording(temp_file)
        dB_result = doppler_effect.calculate_dB_level(temp_file)

        return [match_result.replace('.wav', '') if int(dB_result[0]) > 30 else "No sound matched",
                int(dB_result[0]),
                dB_result[1] if int(dB_result[0]) > 30 else "N/A"]
    else:
        return "failed"

if __name__ == '__main__':
    app.run(host="0.0.0.0")
