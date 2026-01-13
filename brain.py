from tasks import *
from memory import *

def process(command):
    command = command.lower()

    if "open" in command:
        if "chrome" in command:
            open_app("chrome")
            return "Opening Chrome"
        if "calculator" in command:
            open_app("calculator")
            return "Opening Calculator"

    elif "battery" in command:
        return system_status()

    elif "weather" in command:
        city = command.split("in")[-1]
        return weather(city)

    elif "remember" in command:
        task = command.replace("remember", "")
        save_reminder(task.strip())
        return "I have saved your reminder"

    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "")
        return wiki_search(topic)

    else:
        return "Sorry, I don't understand yet"
