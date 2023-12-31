from flask import Flask, render_template, request
import os
import speech_recognition as sr

audiototext = Flask(__name__)

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            return text
    except sr.UnknownValueError:
        return "Speech recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results; {e}"

@audiototext.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', message="No file part")
        
        file = request.files['file']
        
        if file.filename == '':
            return render_template('index.html', message="No selected file")
        
        if file:
            file.save(file.filename)
            text_result = transcribe_audio(file.filename)
            os.remove(file.filename)
            return render_template('index.html', transcript=text_result)
    
    return render_template('index.html')

if __name__ == '__main__':
    audiototext.run(debug=True)
