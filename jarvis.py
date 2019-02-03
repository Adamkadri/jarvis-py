import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests

def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say "+ audio)

    #  use the system's inbuilt say command instead of mpg123
##        text_to_speech = gTTS(text=audio, lang='en')
##        text_to_speech.save('audio.mp3')
##        os.system('mpg123 audio.mp3')


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
 #       r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
#sv-SE
        command = r.recognize_google(audio, language = "en-US").lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command):
    "if statements for executing commands"

    if "what's your name" in command:
        talkToMe('my name is jarvis, and you?')

    elif 'my name is adam' in command:
        talkToMe('nice to meet you adam')
        
    elif '' in command:
        talkToMe('')
    elif '' in command:
        talkToMe('')
    elif '' in command:
        talkToMe('')
    elif '' in command:
        talkToMe('')
    elif '' in command:
        talkToMe('')


    else:
        talkToMe('I don\'t know what you mean!')


#talkToMe('hello sir. how can i help you ?')
talkToMe('hello sir, how can I help you?')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())
