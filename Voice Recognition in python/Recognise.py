print('hello codes')
import speech_recognition as sr
import pyttsx3
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('Hello, I am your Alexa , What can I do for you? Can I get some Dabeli today')
while(1):
        try:
                with sr.Microphone() as source:
                        print('listening...')
                        voice = listener.listen(source)
                        command = listener.recognize_google(voice)
                        command = command.lower()
                        if 'alexa' in command:
                                engine.say(command)
                                engine.runAndWait()
                                print(command)
        except:
                print('error')
