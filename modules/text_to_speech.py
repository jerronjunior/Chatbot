import pyttsx3

def speak_response(response):
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()
