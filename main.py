import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import time

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    if voice.id == 'english-us':
        engine.setProperty('voice', voice.id)
        engine.setProperty('rate', 150)
        engine.setProperty('gender', 'female')
        engine.setProperty('age', 18)
        break

engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            engine.say("hello renish")
            engine.runAndWait()
            voice = listener.listen(source, timeout=3, phrase_time_limit=3)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'system' in command:
                command = command.replace("system", "")
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        command = command.replace('play', '')
        talk("Playing "+ command)
        pywhatkit.playonyt(command)
    elif 'what is' in command:
        command = command.replace('what is ', '')
        if 'time' in command:
            timenow = datetime.datetime.now()
            print("Time is ", str(timenow.strftime("%-I:%M:%S %p")))
            talk("Time is "+ str(timenow.strftime("%-I:%M:%S %p")))
        elif 'date' in command:
            date = datetime.datetime.now()
            print("date is ", str(date.strftime("%A, %d %b %Y")))
            talk("The date is "+ str(date.strftime("%A, %d %b %Y")))
        else:
            pywhatkit.search(command)
    elif "hello" in command:
        talk("what can i do for you")
        run_alexa()
    elif "sleep" in command:
        talk("sleeping")
        time.sleep(500)
        run_alexa()
    else:
        talk("No command was recieved")
        talk("Say sleep to go into sleep mode")
        run_alexa()

run_alexa()
