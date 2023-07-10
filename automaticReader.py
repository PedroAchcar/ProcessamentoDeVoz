import pyttsx3
import json

def automaticReader (json_string):
    speaker = pyttsx3.init()
    speaker.say(json_string)
    speaker.runAndWait()

json_string = json.dumps(meaning)
automaticReader(json_string)
