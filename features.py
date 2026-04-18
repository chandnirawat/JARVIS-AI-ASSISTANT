import os
import webbrowser
import pyttsx3
import pywhatkit as kit
import datetime

# =========================
# ✅ SPEAK
# =========================
engine = pyttsx3.init()

def speak(text):
    try:
        print("Jarvis:", text)
        engine.say(text)
        engine.runAndWait()
    except:
        pass


# =========================
# ✅ OPEN APPS / WEBSITES
# =========================
def opencommand(query):
    query = query.replace("open", "").strip().lower()

    if "youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "google" in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "facebook" in query:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "instagram" in query:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "whatsapp" in query:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")

    elif "notepad" in query:
        speak("Opening Notepad")
        os.system("notepad")

    elif "calculator" in query:
        speak("Opening Calculator")
        os.system("calc")

    elif "chrome" in query:
        speak("Opening Chrome")
        os.system("start chrome")

    else:
        speak("Opening " + query)
        webbrowser.open(f"https://www.{query}.com")


# =========================
# ✅ PLAY YOUTUBE
# =========================
def playyoutube(query):
    try:
        query = query.replace("play", "").strip()
        speak("Playing " + query)
        kit.playonyt(query)
    except:
        speak("Unable to play")


# =========================
# ✅ GOOGLE SEARCH
# =========================
def searchgoogle(query):
    query = query.replace("search", "").strip()
    speak("Searching " + query)
    webbrowser.open(f"https://www.google.com/search?q={query}")


# =========================
# ✅ TIME
# =========================
def telltime():
    time_now = datetime.datetime.now().strftime("%I:%M %p")
    speak("The time is " + time_now)


# =========================
# ✅ DATE
# =========================
def telldate():
    date_now = datetime.datetime.now().strftime("%d %B %Y")
    speak("Today's date is " + date_now)


# =========================
# ✅ MOVIE SEARCH
# =========================
def playmovie(query):
    movie = query.replace("movie", "").replace("play", "").strip()
    speak("Searching movie " + movie)
    webbrowser.open(f"https://www.google.com/search?q={movie}+movie")


# =========================
# ✅ JOKE
# =========================
def telljoke():
    speak("Why did the computer catch a cold? Because it left Windows open!")


# =========================
# ✅ EXIT
# =========================
def exitapp():
    speak("Goodbye")
    exit()