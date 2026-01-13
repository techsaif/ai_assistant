from speech import speak, listen
from brain import process

def main():
    speak("Assistant started")
    while True:
        command = listen()
        if command == "":
            continue
        print("You:", command)

        if "exit" in command or "quit" in command:
            speak("Goodbye")
            break

        response = process(command)
        print("Bot:", response)
        speak(response)

if __name__ == "__main__":
    main()
