from modules.speech_recognition import handle_command_or_chat

def main():
    print("Hello! I'm Jerrom, your assistant!")
    while True:
        handle_command_or_chat()  # All-in-one handler
        print("Say 'exit' to quit.")
        if input("Type 'exit' to quit or press Enter to continue: ").strip().lower() == "exit":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
