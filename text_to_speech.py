import pyttsx3


def automaticReader(texto: str):
    speaker = pyttsx3.init()
    speaker.say(texto)
    speaker.runAndWait()
