import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def talk(text):
    print("🤖:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("🎙️ Listening... (say something within 5 seconds)")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            print("You:", command)
            return command.lower()
        except sr.WaitTimeoutError:
            talk("You didn’t say anything.")
        except sr.UnknownValueError:
            talk("I didn't understand that.")
        except sr.RequestError:
            talk("Service is unavailable.")
        return ""

def run_ai():
    talk("Hi, I'm Nova. How can I help you?")
    while True:
        command = listen()
        if not command:
            continue
        if "time" in command:
            now = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"It’s {now}")
        elif "search" in command:
            topic = command.replace("search", "")
            try:
                result = wikipedia.summary(topic, sentences=2)
                talk(result)
            except:
                talk("I couldn’t find that.")
        elif "play" in command:
            song = command.replace("play", "")
            talk(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)
        elif "exit" in command or "stop" in command or "bye" in command:
            talk("Goodbye!")
            break
        else:
            talk("Sorry, I can't do that yet.")

run_ai()
