import match
from scipy.io.wavfile import write
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

        # sound repository
        folder_path = 'Sounds/'
        result = match.match_recording(temp_file, folder_path)
        return result
    else:
        return "failed！"

if __name__ == '__main__':
    app.run(host="0.0.0.0")
