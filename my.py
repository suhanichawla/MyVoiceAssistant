import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pyaudio

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")

print(voices[0].id)
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if(hour>=0 and hour<12):
        speak("Good morning")
    elif(hour>=12 and hour<18):
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am your VC")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=300
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
        try:
            print("recognizing")
            query=r.recognize_google(audio,language="en-us")
            print(f"user said: {query}")
        except Exception as e:
            print("say that again")
            query=takeCommand().lower()
            return query
        return query

if __name__ == "__main__":
    speak("hello world")
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'your name' in query:
            speak('i am vc')
        elif 'who are you' in query:
            speak("i am vc")
        elif 'wikipedia' in query:
            speak("searching wikipedia")
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('according to wikipedia')
            print(results)
            speak(results)
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"time is {strTime}")
        elif 'open code' in query:
            codePath="vs code path"
            os.startfile(codePath)
        elif 'open song' in query:
            #dir with 3 songs
            music_dir="D:\\songs"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randrange(0,3)]))
        #similarly open other apps 
