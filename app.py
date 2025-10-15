from flask import Flask, render_template, request, jsonify
from deepface import DeepFace # type: ignore
import cv2 # type: ignore
import numpy as np
import io
import librosa # type: ignore
from transformers import pipeline # type: ignore
import base64
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_emotion():
    if 'frame' not in request.files:
        return jsonify({'error': 'No frame uploaded'}), 400

    frame = request.files['frame']
    
    try:
        print("Processing frame...")
        file_bytes = np.frombuffer(frame.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        emotion_results = DeepFace.analyze(img, actions=['emotion'])
        print("Emotion analysis result:", emotion_results)        
        emotions = []
        for result in emotion_results:
            dominant_emotion = result['dominant_emotion']
            emotions.append(dominant_emotion)
        
        return jsonify({'emotions': emotions})
    except Exception as e:
        print("Error processing frame:", str(e))
        return jsonify({'error': str(e)}), 500

@app.route('/record', methods=['POST'])
def record():
    audio_data = request.form['audioData']
    result = classify_audio(audio_data)
    return jsonify(result)

def classify_audio(audio_data):
    audio_data = audio_data.split(",")[-1]
    audio_bytes = base64.b64decode(audio_data)
    with open('temp_audio.wav', 'wb') as f:
        f.write(audio_bytes)
    audio_array, _ = librosa.load('temp_audio.wav', sr=16000)
    pipe = pipeline("audio-classification", model="./wav2vec2-base-Speech_Emotion_Recognition")
    result = pipe(audio_array)
    result = json.dumps(result)
    print("Classification Result:", result)
    os.remove('temp_audio.wav')
    return result

if __name__ == "__main__":
    app.run(debug=True)
    