# Intelligent Digital Assistant (IDA) - Speech

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import pywhatkit
import pyjokes
#printing statement 
print('Loading your personal assistant - IDA')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            statement = r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


speak("Loading your personal assistant IDA")
wishMe()


if __name__ == '__main__':
    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant IDA is shutting down,Good bye')
            print('your personal assistant IDA is shutting down,Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'open notepad' in statement:
            name = statement.replace('open', '')
            path0 = f"%windir%\\system32\\notepad.exe"
            os.system(path0)

        elif 'open wordpad' in statement:
            name = statement.replace('open', '')
            path0 = f"%windir%\\system32\\wordpad.exe"
            os.system(path0)

        elif 'open word' in statement:
            name = statement.replace('open', '')
            path0 = f"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.system(path0)

        elif 'open powerpoint' in statement:
            name = statement.replace('open', '')
            path0 = f"C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.system(path0)

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am IDA your personal assistant. I am programmed to do minor tasks like'
                  'opening youtube,google chrome,gmail and predict time,')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by DK AND MADHU")
            print("I was built by DK AND MADHU")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'play' in statement:
            song = statement.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'joke' in statement:
            speak(pyjokes.get_joke())

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])


        elif"weather" in statement:
             speak("finding the weather")
             webbrowser.open_new_tab("https://www.windy.com/?12.900,80.221,5")
            
         



time.sleep(3)
