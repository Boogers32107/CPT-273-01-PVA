# CPT-273-01-PVA


This Personal Voice assistant is activated with "Jarvis" even though his name is "Steve" because I couldn't get the Porcupine Custom Keywords to work and didn't have time to troubleshoot it. The PVA can be asked for: 

1. A Trivia Fact 

2. The Weather 

3. The time 

4. The Day 

5. A Joke 

They are activated by simply saying the Word or saying Tell me followed by the Keyword: Trivia, Joke, Weather, Time, Day, etc... 

Some resources that I used to figure out how to create a PVA where 

Circular Dynasty. How to make your own voice assistance in Python. Medium. Retrieved April 6, 2025, from https://medium.com/@circular.dynasty/how-to-make-your-own-voice-assistance-in-python-b8979a8f9b53 

GeeksforGeeks. Voice assistant using Python. Retrieved April 6, 2025, from https://www.geeksforgeeks.org/voice-assistant-using-python/ 


The hardest part for me was just getting IDLE to work with Speech Recognition for whatever reason it just would not work until I uninstalled it and reinstalled IDLE and then redownloaded the Pip install stuff for it to work once it worked it was somewhat smooth sailing until the API pulls gave me a bit of trouble but other than that it just took a lot of time to work out getting stuff working and then having it hear my microphone. 

For Future improvement it would be really neat to get the OPENAI.API but it costs money cause then you would only need one API pull as it could tell time, weather, date, news, jokes, trivia and whatever else you could want... but it costs money and I am broke so not going to happen. 

Also, it does have continuous listening, it just reruns itself when it finishes it's cycle. 

Links for APIs used: 
https://openweathermap.org/  
https://opentdb.com/  
https://picovoice.ai/  

List of Imports  
import requests  
import pvporcupine  
import pyaudio  
import struct  
import speech_recognition  
import pyttsx3  
import html  
import datetime 

PIP Install requirements 

pip install requests  
pip install pvporcupine  
pip install pyaudio pip  
install SpeechRecognition  
pip install pyttsx3 


PIP Install requirements

pip install requests
pip install pvporcupine
pip install pyaudio
pip install SpeechRecognition
pip install pyttsx3