print('hello codes')
import speech_recognition as sr
import pyttsx3
# print(dir(sr))
# print('test')
listener = sr.Recognizer()
# print('test')
while(True):
        with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                # print(command)
                command = command.lower()
                if 'alexa' in command:
                   print(command)

