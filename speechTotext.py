from cgitb import text
from email.mime import audio
import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print('Say something: ')
    audio= r.listen(source)

    try:
        text=r.recognize_google(audio)
        print('Dijiste: {}'.format(text))
    except:
        print('lo siento no escuche bien')