$(document).ready(function () {

    // Text animation
    if ($.fn.textillate) {
        $('.text').textillate({
            loop: true,
            sync: true,
            in: { effect: "bounceIn" },
            out: { effect: "bounceOut" }
        });
    }

    // SiriWave Configuration (Single Instance)
    if (typeof SiriWave !== "undefined" && !window.siriWave) {
        window.siriWave = new SiriWave({
            container: document.getElementById("siri-container"),
            width: 800,
            height: 200,
            style: "ios9",
            amplitude: 1,
            speed: 0.3,
            autostart: false
        });
    }

    // Mic button click
    $("#micbtn").off("click").on("click", async function () {

        console.log("Mic clicked");

        $("#oval").hide();
        $("#siriwave").show();

        // ✅ Wave start
        if (window.siriWave) window.siriWave.start();

        // ✅ Show Listening immediately
        $(".siri-message").text("Listening...");

        try {
            if (typeof eel !== "undefined" && eel.allCommands) {

                // ✅ Call Python function using async/await
                const finalCommand = await eel.allCommands()();

                // ✅ Recognizing message
                $(".siri-message").text("Recognizing...");

                setTimeout(function(){
                    if(finalCommand && finalCommand !== ""){
                        // ✅ Show the command that is being executed
                        $(".siri-message").text(finalCommand);
                    } else {
                        $(".siri-message").text("Nothing heard");
                    }

                    // ✅ Stop wave and reset
                    if (window.siriWave) window.siriWave.stop();
                    $("#siriwave").hide();
                    $("#oval").show();

                }, 500); // small delay for realism

            } else {
                console.log("Eel not loaded");
                if (window.siriWave) window.siriWave.stop();
                $("#siriwave").hide();
                $("#oval").show();
            }

        } catch(err) {
            console.error("Eel call error:", err);
            $(".siri-message").text("Error executing command");
            if (window.siriWave) window.siriWave.stop();
            $("#siriwave").hide();
            $("#oval").show();
        }
    });

});


/*import pyttsx
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyautogui
import pywhatkit

# ---------------- VOICE SETUP ----------------
engine = pyttsx3.init()
engine.setProperty('rate', 170)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    print("Jarvis:", text)
    try:
        engine.say(text)
        engine.runAndWait()
    except:
        pass


# ---------------- WISH ----------------
def wish():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis. How can I help you")


# ---------------- TAKE COMMAND ----------------
def take_command():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")

            r.adjust_for_ambient_noise(source, duration=1)
            r.pause_threshold = 0.8

            audio = r.listen(source, timeout=4, phrase_time_limit=5)

    except sr.WaitTimeoutError:
        return "none"
    except Exception as e:
        print("Mic Error:", e)
        return "none"

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        return "none"

    except sr.RequestError:
        speak("Internet not working")
        return "none"

    except Exception as e:
        print("Error:", e)
        return "none"


# ---------------- MAIN ----------------
if __name__ == "__main__":

    wish()

    while True:
        command = take_command()

        if command == "none":
            continue

        # EXIT
        if "exit" in command or "stop" in command or "bye" in command:
            speak("Goodbye")
            break

        # YOUTUBE
        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        # GOOGLE
        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        # PLAY SONG
        elif "play" in command:
            song = command.replace("play", "").strip()

            if song == "":
                speak("What should I play")
            else:
                speak("Playing " + song)
                try:
                    pywhatkit.playonyt(song)
                except:
                    speak("Unable to play song")

        # TIME
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak("The time is " + current_time)

        # DATE
        elif "date" in command:
            today = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today is " + today)

        # WIKIPEDIA
        elif "wikipedia" in command:
            speak("Searching Wikipedia")
            query = command.replace("wikipedia", "").strip()

            if query == "":
                speak("What should I search")
            else:
                try:
                    result = wikipedia.summary(query, sentences=2)
                    speak(result)
                except:
                    speak("No result found")

        # NOTEPAD
        elif "open notepad" in command:
            speak("Opening Notepad")
            os.system("notepad")

        # CHROME
        elif "open chrome" in command:
            speak("Opening Chrome")
            os.system("start chrome")

        # SCREENSHOT
        elif "screenshot" in command:
            try:
                img = pyautogui.screenshot()
                img.save("screenshot.png")
                speak("Screenshot taken")
            except:
                speak("Unable to take screenshot")

        else:
            speak("I did not understand")*/