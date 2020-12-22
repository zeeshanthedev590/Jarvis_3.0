# Modules

import os
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pyjokes
import webbrowser
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(speech):
    engine.say(speech)
    engine.runAndWait()


def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk('Good Morning')
    elif hour >= 12 and hour < 18:
        talk('Good AfterNoon')
    else:
        talk('Good Evening')

    talk('How May Help You')


def listen():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1

        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()
        if 'jarvis' in query:
            query = query.replace('jarvis', '')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def run_jarvis():
    while True:
        query = listen()
        if 'play' in query:
            song = query.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)

        if 'wikipidia' in query or 'search' in query or 'look' in query or 'find' in query:
            talk('Searching WikiPidia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            talk("According to Wikipedia")
            print(results)
            talk(results)

        elif 'youtube' in query:
            webbrowser.open("http://youtube.com")
        elif 'google' in query:
            webbrowser.open("http://google.com")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            talk(f"The Time Is {strTime}")

        elif 'joke' in query:
            talk(pyjokes.get_joke())

        elif 'bye' in query:
            talk('Bye Bye')
            exit()
        else:
            print('Please say the command again.')


def main():
    """
    This Is the Main Function Of The Programs
    """
    greetings()
    run_jarvis()


if __name__ == "__main__":
    main()
