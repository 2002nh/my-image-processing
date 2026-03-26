#AI Assistant
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
r = sr.Recognizer()
phone_number={"mommy":"09128612184","daddy":"09123655021","aunt":"09125679309"}
def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('Listening... Ask now...')
            audioin = r.listen(source)
            my_text= r.recognize_google(audioin)
            my_text=my_text.lower()
            print(my_text)
            speak(my_text)
            # ask to play song 
            if 'play' in my_text:
                my_text = my_text.replace('play','')
                speak('playing' + my_text)
                pywhatkit.playonyt(my_text)
            # ask date
            elif 'date' in my_text:
                today = datetime.date.today()
                speak(str(today))
            # ask time
            elif 'time' in my_text:
                timenow = datetime.datetime.now().strftime("%H:%M")
                speak(timenow)
            # ask details about any person
            elif 'tell about' in my_text:
                person = my_text.replace('tell about','')
                info = wikipedia.summary(person,1)
                speak(info)
            # ask phone numbers
            elif 'phone number' in my_text:
                names = list(phone_number)
                for name in names:
                    if name in my_text:
                        print(name+" phone number is "+phone_number[name])
                        speak(name+" phone number is "+phone_number[name])
            elif 'love you' in my_text:
                speak('ooooh i love you too cutie pie')
    except:
        print("Error in capturing microphone...")
while True:
    commands()