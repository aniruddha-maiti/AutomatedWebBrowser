#Import necessary packages
#Import speech recognition
import speech_recognition as sr
#Import web Browser
import webbrowser as wb
#Import matplot
import matplotlib.pyplot as plt
#Import numpy
import numpy as np
import wave, sys

#create 4 instances of recognizer
r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
r4 = sr.Recognizer()

#Process for storing and recognizing speech
with sr.Microphone() as source:
    print('[search Twitter: search youtube: search Facebook]')
    print('speak now')
    #Adjust the noise of the source
    r3.adjust_for_ambient_noise(source)
    #Store the pseech in this variable
    audio = r3.listen(source)
    #Print the speech in text by recognizing it
    print(r2.recognize_google(audio))

#Check if the spoken word is "Facebook", if yes then open facebook
if 'Facebook' in r4.recognize_google(audio):
    wb.open_new('https://www.facebook.com/')

#Check if the spoken word is "Twitter", if yes then open twitter
if 'Twitter' in r2.recognize_google(audio):
    wb.open_new('https://twitter.com/home')

#Check if the spoken word id "Video", if yes then open Youtube.
if 'video' in r1.recognize_google(audio):
    r1 = sr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    #Here we will ask what the user wants to search in youtube
    with sr.Microphone() as source:
        print('search your query')
        r1.adjust_for_ambient_noise(source)
        #Store the query of the user.
        audio = r1.listen(source)

        try:
            get = r1.recognize_google(audio)
            print("taking the i/p: ")
            print(get)
            #The new url that we have to open is the concat string with the youtube link and search query.
            wb.get().open_new(url + get)
        #if not found then throw error
        except sr.UnknownValueError:
            print('error')
       #Throw failed message when there is an error when s/w is taking the query
        except sr.RequestError as e:
            print('failed'.format(e))
