import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime,re

engine = pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id)
text ='Hello, I am your Alex'
def talk(text):
        engine.say(text)
        engine.runAndWait()
listener = sr.Recognizer()
print('hello codes')

def take_command():
                        with sr.Microphone() as source:
                                        print('listening...')
                                        voice = listener.listen(source)
                                        command = listener.recognize_google(voice)
                                        command = command.lower()
                                        talk('You said'+ command)
                                        if 'alex' in command:
                                                command = command.replace('alex','')
                                                print(command)
                                                return command
                                        else:
                                                print('Not received command')
                                                print(command)
                                                return ''
    
def run_alexa():
        talk('What can I do for you')  
        command=take_command()
        if 'play' in command:
                song = re.sub(".*\splay\s", "", command)
                print(song)
                talk('playing'+song)
                pywhatkit.playonyt(song)
        elif 'time' in command and 'now' in command:
                time = datetime.datetime.now().strftime('%H:%M:%p')
                talk('Time right now is '+time)
        elif 'date today' in command:
                date = datetime.datetime.now().strftime("%A:%d:%B:%Y")
                talk('The Date today is'+date)
        elif 'how are you' in command:
                talk('I am good thank you How about you')
        elif 'i am' in command or 'i\'m' in command:
                talk('Alright I see')
        elif 'sleep' in command:
                return 'sleep'
        else:
                talk('Could not recognize what you just said please Repeat')
        return 'repeat'

talk(text)
try:
        while(text!='sleep'):
                text=run_alexa()
                print('loop:')
                print(text)               
        talk('Bye Bye')
except KeyboardInterrupt:
        talk('Bye Bye')
except Exception as e:
        print(e)
        talk('Some error occurred')

