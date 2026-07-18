import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import os 
import wikipedia 
import requests 
import Ai


from datetime import datetime
recognizer = sr.Recognizer()
engine = pyttsx3.init()

import os
from dotenv import load_dotenv

load_dotenv()

news_api = os.getenv("NEWS_API_KEY")


def get_news():

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}"

    response = requests.get(url)
    data = response.json()

    return data


def speak(text):
    global engine
    engine.stop()
    engine.say(text)
    engine.runAndWait()

def processCommand(c)  :
    if "open google" in c.lower() :
        webbrowser.open("https://google.com") 
    
    elif "open youtube" in c.lower() :
        webbrowser.open("https://www.youtube.com/")

    elif "open linkedin" in c.lower() :
        webbrowser.open("https://www.linkedin.com/in/jaivardhan-singh-4a69b8380/?skipRedirect=true")

    elif "open instagram" in c.lower() :
        webbrowser.open("https://www.instagram.com/?hl=en")
    
    elif "open github" in c.lower() :
        webbrowser.open("https://github.com/")

    elif c.lower().startswith("play") :
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "time" in c.lower():
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in c.lower():
        print("Date block reached")
        current_date = datetime.now().strftime("%d %B %Y")
        print(current_date)
        speak(f"Today's date is {current_date}")

    elif c.lower().startswith("search"):
        query = c[7:].strip()
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif c.lower().startswith("google"):
        query = c[7:].strip()
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif c.lower().startswith("youtube"):
        query = c[8:].strip()
        speak(f"Searching YouTube for {query}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

    
    elif "open notepad" in c.lower():
        speak("Opening Notepad")
        os.startfile("notepad.exe")

    elif "open calculator" in c.lower():
        speak("Opening Calculator")
        os.startfile("calc.exe")

    elif "open paint" in c.lower():
        speak("Opening Paint")
        os.startfile("mspaint.exe")
    
    elif c.lower().startswith("who is"):
        person = c[7:].strip()

        try:
            result = wikipedia.summary(person, sentences=2)
            speak(result)
        except:
            speak("Sorry, I couldn't find information.")

    elif "news" in c.lower():
        try:
            speak("Fetching today's news.")

            news = get_news()
            articles = news["articles"]

            for i, article in enumerate(articles[:5], start=1):
                print(f"{i}. {article['title']}")
                speak(article["title"])

        except Exception:
            speak("Sorry, I couldn't fetch the news.")

    else :
        try:
            speak("Thinking...")
            answer = Ai.ask_gemini(c)
            print(answer)
            speak(answer)
        except Exception:
            speak("Sorry, I couldn't connect to Gemini.")


if __name__ == "__main__" :
    speak("Initializing Jarvis....")
    while True:

        # Listen for the wake word "Jarvis"

        # obtain audio from the microphone 
        r = sr.Recognizer()
        

        print("Recognizing....")
        # Recognize speech using Jarvis 
        try :
            with sr.Microphone() as source :
                print("Listening....")
                audio = r.listen(source,timeout = 5 , phrase_time_limit = 5)
            word = r.recognize_google(audio)
            print(word)
            if(word.lower() == "panda") :
                speak("Yes Sir!")
                # Listen for command 

                with sr.Microphone() as source :
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(command)
                    processCommand(command)


        
        except sr.UnknownValueError:
            print("Audio cann't identified!")

        except sr.RequestError as e :
            print("Error : {0}".format(e))
