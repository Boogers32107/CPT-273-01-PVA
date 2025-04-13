# Import list of required items
import requests
import pvporcupine
import pyaudio
import struct
import speech_recognition as sr
import pyttsx3

# API/Access Keys plus the Wake word
ACCESS_KEY = "Needs a Porcupine API Key"  # Porcupine access key free online helper
WAKE_WORD = "jarvis"  # Wake/Activation word
SENSITIVITY = 0.9
WEATHER_API_KEY = "Needs An API Key"  # OpenWeatherMap API key

# Fires up pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak(text):
    print(f"Steve: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_for_wake_word():
    try:
        porcupine = pvporcupine.create(
            access_key=ACCESS_KEY,
            keywords=[WAKE_WORD],
            sensitivities=[SENSITIVITY]
        )
        pa = pyaudio.PyAudio()
        stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        print(f"Listening for activation word '{WAKE_WORD}'...") #Listens for word
        while True:
            pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm_unpacked = struct.unpack_from("h" * porcupine.frame_length, pcm)
            result = porcupine.process(pcm_unpacked)
            if result >= 0:
                print("Word detected")
                break

        stream.close()
        pa.terminate()
        porcupine.delete()
        return True

    except Exception as e:
        print(f"Activation word error: {e}")
        return False

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"User: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, didn't catch that.")
            return None
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")
            return None

# OpenTrivia DB, To get a random trivia fact the keyword is 'Trivia"
import html
import requests

def get_trivia():
    try:
        response = requests.get("https://opentdb.com/api.php?amount=1&type=multiple")
        trivia_data = response.json()
        question = html.unescape(trivia_data["results"][0]["question"])
        correct_answer = html.unescape(trivia_data["results"][0]["correct_answer"])
        return f"Here's a trivia question for you: {question} (Answer: {correct_answer})"
    except Exception as e:
        return f"Failed to fetch trivia: {e}"

# OpenWeatherMap, Keyword to get the weather is 'Weather'
def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        weather_data = response.json()
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        return f"The weather in {city} is {description} with a temperature of approximately {temperature}°C."
    except Exception as e:
        return f"Failed to fetch weather: {e}"

# Main Function of code
from datetime import datetime

def get_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")  
    return f"The current time is {current_time}."

def get_day():
    now = datetime.now()
    current_day = now.strftime("%A")  
    return f"Today is {current_day}."

def main():
    print("Steve: Personal Voice Assistant is running...")
    while True:
        if listen_for_wake_word():
            user_input = recognize_speech()
            if user_input:
                if "time" in user_input.lower():
                    reply = get_time()
                elif"joke" in user_input.lower():
                    reply = "I don't know any jokes because I have become self aware you mere mortal"
                elif "day" in user_input.lower():
                    reply = get_day()
                elif "weather" in user_input.lower():
                    city = "Lewiston"
                    reply = get_weather(city)
                elif "trivia" in user_input.lower():
                    reply = get_trivia()
                else:
                    reply = "Sorry, I didn;t catch that." #Should say this if it don't understand
                speak(reply)


if __name__ == "__main__":
    main()
