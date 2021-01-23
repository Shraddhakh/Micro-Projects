print('hello codes')
import speech_recognition as sr
print(dir(sr))
print('test')
listener = sr.Recognizer()
print('test')
with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
