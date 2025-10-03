import speech_recognition as sr
import win32com.client
import webbrowser
from musicLibrary import music_library

def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def AI(prompt):
    try:
        query = prompt.replace(" ", "+")
        url = f"https://www.google.com/search?q={query}"
        say("Searching Google for you")
        webbrowser.open(url)
        return "Here are the search results I found on Google."
    except Exception as e:
        return f"Sorry, I couldn't get results from Google. Error: {e}"

def takeCommand(timeout=5):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=timeout)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            print(f"Speech recognition request failed: {e}")
            return ""
        except Exception as e:
            print(f"Error: {e}")
            return ""

sites = [
    ["youtube", "https://www.youtube.com"],
    ["google", "https://www.google.com"],
    ["wikipedia", "https://www.wikipedia.com"],
    ["facebook", "https://www.facebook.com"],
    ["instagram", "https://www.instagram.com"],
    ["twitter", "https://twitter.com"],
    ["linkedin", "https://www.linkedin.com"],
    ["reddit", "https://www.reddit.com"],
    ["tiktok", "https://www.tiktok.com"],
    ["pinterest", "https://www.pinterest.com"],
    ["quora", "https://www.quora.com"],
    ["snapchat", "https://www.snapchat.com"]
]

wake_word = "hello max"

if __name__ == "__main__":
    say("Initializing Max. Say 'Hello Max' to wake me up.")
    active = False

    while True:
        text = takeCommand()
        if text == "":
            continue

        if wake_word in text and not active:
            active = True
            say("Yes sir")
            continue
        elif wake_word in text and active:
            active = False
            say("Going to sleep. Say wake word to wake me up again.")
            continue

        if active:
            for site in sites:
                if f"open {site[0]}" in text:
                    say(f"Opening {site[0]} for you")
                    webbrowser.open(site[1])

            if "play" in text:
                song_name = text.replace("play", " ").strip()
                if song_name in music_library:
                    say(f"Playing {song_name}")
                    webbrowser.open(music_library[song_name])
                else:
                    say(f"Sorry, I could not find {song_name} in the library")

            if "max ji" in text or "chat" in text:
                ai_response = AI(prompt=text)
                say(ai_response)
