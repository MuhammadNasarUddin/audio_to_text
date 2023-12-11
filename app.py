import streamlit as st
import speech_recognition as sr

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Speech recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results; {e}"

def main():
    st.title("Audio to Text Converter")

    uploaded_file = st.file_uploader("Upload an audio file", type=["wav"])

    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/wav')
        if st.button("Transcribe"):
            with st.spinner("Transcribing..."):
                text_result = transcribe_audio(uploaded_file)
                st.write("Transcript:", text_result)

if __name__ == "__main__":
    main()




