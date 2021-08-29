import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
import smtplib
engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)

def speak(audio):
       engine.say(audio)
       engine.runAndWait()      

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")    
    speak("I am jarvis Sir, Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output       
     r=sr.Recognizer()
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
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password-here')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if __name__=="__main__" :
 wishme()
 #speak("Rahul is a good Boy")
 while True:
    query=takeCommand().lower()#Logic for executing task based on query
    
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")    
    elif 'play music' in query:
        music_dir='-the-path-of-your-music-dir'
        songs=os.listdir(music_dir)
        #print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
    elif 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Sir, The time is {strTime}")
        speak(f"Sir, The time is {strTime}")
    elif 'open code' in query:
         codepath="the-path-of-your-editor"
         os.startfile(codepath)  
    elif 'email to rahul' in query:
        try:
            speak("What should i say?")
            content=takeCommand()
            to="rahul.krcusat@gmail.com"
            sendEmail(to,content)
            speak("Email has been Sent!")
        except Exception as e:
            print(e)
            speak("Sorry my friend rahul bhai. I am not able to send this email")
    elif 'quit' in query:
        speak("Bye Sir, Have a good day")
        exit()

 
