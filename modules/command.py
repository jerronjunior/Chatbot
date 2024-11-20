import webbrowser
import datetime
import random

def process_command(command):
    """
    Handles predefined commands like opening websites, checking time, etc.
    """
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}."
    
    elif "date" in command:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today}."
    
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."
    
    elif "play music" in command:
        webbrowser.open("https://open.spotify.com/")
        return "Playing music on Spotify."
    
    elif "joke" in command:
        jokes = [
            "Why don’t skeletons fight each other? Because they don’t have the guts!",
            "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.",
        ]
        return random.choice(jokes)
    
    elif "fact" in command:
        facts = [
            "Did you know? The Eiffel Tower can be 15 cm taller during the summer due to heat.",
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old!",
        ]
        return random.choice(facts)
    
    return None
