import speech_recognition as sr

def speech2Text(AUDIO_FILE):
    recognizer = sr.Recognizer()

    with sr.AudioFile(AUDIO_FILE) as source:
        audio = recognizer.record(source)

    result = recognizer.recognize_google(audio)
    return result
