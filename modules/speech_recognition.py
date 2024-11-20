import speech_recognition as sr
from modules.commands import process_command
from modules.chatbot import chatbot_response
from modules.text_to_speech import speak_response

def listen_to_user():
    """
    Captures voice input, processes commands, and routes non-commands to the chatbot.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            speak_response("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            print("Network error.")
            speak_response("I'm having trouble connecting to the network.")
            return None

def handle_command_or_chat():
    """
    Listens for user input, checks for predefined commands, and defaults to chatbot for other queries.
    """
    command = listen_to_user()
    if command:
        # Check predefined commands
        response = process_command(command)
        if response:
            print(f"Jerrom: {response}")
            speak_response(response)
        else:
            # Pass to chatbot for other queries
            response = chatbot_response(command)
            print(f"Jerrom: {response}")
            speak_response(response)
