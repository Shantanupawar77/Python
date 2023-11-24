import webbrowser
from numpy import source
import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>0 and hour<12:
        speak("Good Morning")
    elif hour >=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am jarvis sir.please tell me how may i help you.")
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__=="__main__":
    #speak(" Dhoni finishesh off his style india left the world cup after 28 years party starting in the dressing room ")
    wishMe()
    while True:

        query=takeCommand().lower()
        if('wikipedia' in query ):
            print("Searching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("Accoring to the wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
            
        elif 'quit jarvis' in query:
            exit()
            
        # elif 'open code'in query:
        #     codePath='C:\\Users\LENOVO\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs' here we have to write the target
        #     os.startfile(codePath)