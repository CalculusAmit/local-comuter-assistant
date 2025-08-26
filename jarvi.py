import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import pywhatkit
import wikipedia
import pyautogui
import time

# --- Speak Function ---
def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

# --- Command Listener ---
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=5)
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception:
            print("Sorry, could not recognize. Say again please...")
            return "None"
    return query.lower()

# --- Wishes user according to the time globally ---
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! Amit")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! Amit")
    else:
        speak("Good Evening! Amit")

# --- Main Program ---
if __name__ == "__main__":
    wishMe()
    speak("Initializing Jarvis... I am Jarvis. How can I help you?")

    exit_commands = ["exit", "quit", "ok bye", "thank you"]

    while True:
        query = takeCommand()

        if "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "search youtube" in query:
            speak("What should I play on YouTube?")
            search_query = takeCommand()
            if search_query != "None":
                speak(f"Playing {search_query} on YouTube")
                pywhatkit.playonyt(search_query)

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "search google" in query:
            speak("What should I search on Google?")
            search_query = takeCommand()
            if search_query != "None":
                speak(f"Searching Google for {search_query}")
                search_url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
                webbrowser.open(search_url)

        elif "open code" in query:
            speak("Opening Visual Studio Code")
            codePath = "d:/python"
            os.startfile(codePath)

        elif "open whatsapp chat" in query:
            speak("Whom should I open chat with?")
            name = takeCommand().lower()
            contacts = {
                "father": "+919954601630",
                "rahul": "+911234567890",
                "mom": "+919876543210"
            }
            found = None
            for key in contacts.keys():
                if key in name:
                    found = key
                    break
            if found:
                phone_number = contacts[found]
                speak(f"Opening WhatsApp chat with {name}")
                webbrowser.open(f"https://wa.me/{phone_number}")
            else:
                speak("Sorry, I don't have that contact saved")

        # --- Closing tabs or apps ---
        elif "close youtube" in query or "close google" in query:
            speak("Closing current tab")
            pyautogui.hotkey("ctrl", "w")

        elif "close recent app" in query:
            speak("Closing recent app")
            pyautogui.hotkey("alt", "f4")

        elif "close microsoft" in query or "close microsoft edge" in query:
            os.system("taskkill /f /im msedge.exe")
            speak("Microsoft Edge closed")

        elif "close brave" in query:
            os.system("taskkill /f /im brave.exe")
            speak("Brave browser closed")

        # --- Wikipedia search ---
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            try:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.DisambiguationError as e:
                speak("There are multiple results, please be more specific.")
                print(e.options[:5])
            except wikipedia.PageError:
                speak("Sorry, I could not find any results for your query.")
            except Exception as e:
                speak("An error occurred while fetching from Wikipedia.")
                print(e)

        # --- Exit command (case-insensitive) ---
        elif any(word in query for word in exit_commands):
            speak("Goodbye Amit, shutting down")
            speak("See you next time")
            break

