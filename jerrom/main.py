from modules.speech_recognition import listen_to_user
from modules.chatbot import chatbot_response
from modules.text_to_speech import speak_response

def main():
    print("JARVIS is now active!")
    while True:
        # Get user input through voice
        command = listen_to_user()
        if command:
            if "exit" in command or "quit" in command:
                print("Goodbye!")
                break
            
            # Get chatbot response
            response = chatbot_response(command)
            print(f"JARVIS: {response}")
            
            # Speak the response
            speak_response(response)

if __name__ == "__main__":
    main()
