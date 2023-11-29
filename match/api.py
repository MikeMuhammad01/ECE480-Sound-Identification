import match
import doppler_effect
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
