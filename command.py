import pyttsx3
import speech_recognition as sr
import eel
import time
import datetime
import webbrowser
import pywhatkit as kit
import requests
import atexit
import os

# =========================
# ✅ ENGINE SETUP
# =========================
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 174)

def speak(text):
    try:
        print("Jarvis:", text)
        eel.displayMessage(text)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("TTS Error:", e)

def cleanup():
    try:
        engine.stop()
    except:
        pass

atexit.register(cleanup)


# =========================
# ✅ TAKE COMMAND
# =========================
def takecommand():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            eel.displayMessage("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)

            audio = r.listen(source, timeout=8, phrase_time_limit=5)

    except Exception as e:
        print("Mic Error:", e)
        return ""

    try:
        print("Recognizing...")
        eel.displayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User:", query)
        eel.displayMessage(query)
        return query.lower()

    except Exception:
        return ""


# =========================
# ✅ COMMAND HANDLER
# =========================
@eel.expose
def allCommands():

    query = takecommand()

    if query == "":
        speak("I didn't hear anything")
        eel.showHood()
        return

    # -------------------------
    # OPEN APPS / WEBSITES
    # -------------------------
    elif "open" in query:
        if "youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")

        elif "google" in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif "facebook" in query:
            webbrowser.open("https://www.facebook.com")
            speak("Opening Facebook")

        elif "instagram" in query:
            webbrowser.open("https://www.instagram.com")
            speak("Opening Instagram")

        elif "whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com")
            speak("Opening WhatsApp")

        elif "notepad" in query:
            os.system("notepad")
            speak("Opening Notepad")

        elif "calculator" in query:
            os.system("calc")
            speak("Opening Calculator")

        else:
            speak("Opening " + query)
            webbrowser.open(f"https://www.{query}.com")

    # -------------------------
    # PLAY SONG / VIDEO
    # -------------------------
    elif "play" in query:
        try:
            song = query.replace("play", "")
            speak("Playing " + song)
            kit.playonyt(song)
        except:
            speak("YouTube error")

    # -------------------------
    # MOVIE SEARCH
    # -------------------------
    elif "movie" in query:
        movie = query.replace("movie", "").strip()
        speak("Searching movie " + movie)
        webbrowser.open(f"https://www.google.com/search?q={movie}+movie")

    # -------------------------
    # GOOGLE SEARCH
    # -------------------------
    elif "search" in query:
        search = query.replace("search", "")
        speak("Searching " + search)
        webbrowser.open(f"https://www.google.com/search?q={search}")

    # -------------------------
    # TIME
    # -------------------------
    elif "time" in query:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        speak("Time is " + time_now)

    # -------------------------
    # DATE
    # -------------------------
    elif "date" in query:
        date_now = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today is " + date_now)

    # -------------------------
    # WEATHER
    # -------------------------
    elif "weather" in query:
        try:
            res = requests.get("https://wttr.in/?format=3", timeout=3)
            speak(res.text)
        except:
            speak("Weather not available")

    # -------------------------
    # JOKE
    # -------------------------
    elif "joke" in query:
        speak("Why did the computer get cold? Because it left Windows open!")

    # -------------------------
    # SYSTEM CONTROL
    # -------------------------
    elif "shutdown" in query:
        speak("Shutting down system")
        os.system("shutdown /s /t 5")

    elif "restart" in query:
        speak("Restarting system")
        os.system("shutdown /r /t 5")

    # -------------------------
    # EXIT
    # -------------------------
    elif "exit" in query or "stop" in query:
        speak("Goodbye")
        exit()

    # -------------------------
    # DEFAULT
    # -------------------------
    else:
        speak("Command not recognized")

    eel.showHood()