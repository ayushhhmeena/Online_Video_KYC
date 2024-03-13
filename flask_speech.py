from flask import Flask, request, jsonify, render_template
import speech_recognition as sr
import re
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Temporary folder to store audio files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        filename = secure_filename(file.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)
        return jsonify(extract_info_from_audio(save_path))

def extract_info_from_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        
    # Your existing `extract_info` function goes here
    # Extract the necessary information
    name, dob, address = extract_info(text)  # Assume `extract_info` is defined

    # Return the extracted information as JSON
    return {
        'name': name,
        'dob': dob,
        'address': address
    }

def extract_info(text):
    # Your existing `extract_info` function implementation
    # Make sure to define the regex patterns and return the extracted values
    pass

if __name__ == '__main__':
    app.run(debug=True)
