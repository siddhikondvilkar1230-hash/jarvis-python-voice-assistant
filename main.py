
import speech_recognition as sr
import webbrowser
import pyttsx3
import sounddevice as sd
from datetime import datetime

# Voice engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

# Jarvis speaks
def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def speak(text):
    print("Jarvis:", text)  # Screen par reply
    engine.say(text)        # Voice mein reply
    engine.runAndWait()     # Voice complete hone tak wait

# Speech recognizer
recognizer = sr.Recognizer()

# Take voice command
def take_command():

    try:
        print("\nListening... Speak now!")

        device = sd.query_devices(kind="input")
        samplerate = int(device["default_samplerate"])

        audio = sd.rec(
            int(5 * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        print("Recognizing...")

        audio_data = sr.AudioData(
            audio.tobytes(),
            samplerate,
            2
        )

        command = recognizer.recognize_google(
            audio_data,
            language="en-IN"
        )

        print("You said:", command)

        return command.lower()

    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return ""

    except sr.RequestError as e:
        print("Google service error:", e)
        return ""

    except Exception as e:
        print("Microphone error:", e)
        return ""


# Jarvis starts
speak("Hello Siddhi. I can speak now.")

while True:

    command = take_command()

    if "hello" in command or "hi" in command:
        speak("Hello Siddhi! How can I help you?")

    elif "your name" in command:
        speak("My name is Jarvis. I am your personal assistant.")

    elif "how are you" in command:
        speak("I am fine. Thank you for asking.")

    elif "what can you do" in command:
        speak("I can open Google, YouTube and tell you the time.")

    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "stop" in command or "exit" in command:
        speak("Goodbye Siddhi! Have a nice day.")
        break

    elif command:
        speak("Sorry, I don't know that command.")
