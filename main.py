import speech_recognition as sr
import webbrowser
import sounddevice as sd
import pyttsx3
import musicLibrary
import requests
import re
import pyautogui
import os
import datetime
import time
from dotenv import load_dotenv

#loading environment varibles from .env
load_dotenv()
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
WEATHER_API_KEY=os.getenv("WEATHER_API_KEY")
NEWS_API_KEY=os.getenv("NEWS_API_KEY")
 
r=sr.Recognizer()
engine=pyttsx3.init()

#speak function
def speak(text):
    engine.stop()
    engine.say(text)
    engine.runAndWait()

#function for ai process
def aiProcess(command):
    command_modified=command+". Please answer in short"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
    data = {
        "contents": [
            {"parts": [{"text": command_modified}]}
        ],
        "generationConfig": {
            "maxOutputTokens": 1200,   # limit response length
            "temperature": 0.7        # creativity control
        }
    }

    response = requests.post(url, json=data)
    if response.status_code == 200:
        result = response.json()
        ai_reply = result["candidates"][0]["content"]["parts"][0]["text"]
        speak("AI:"+ai_reply)
        print("AI:"+ai_reply)
    else:
        speak("Error from Gemini:"+ response.text)
        speak("Sorry, I couldn't process that with AI.")

#safe speak function
def safe_speak(text):
    if text:
        # Remove non-ASCII characters (like emojis)
        clean_text = re.sub(r'[^\x00-\x7F]+', ' ', text)
        # Replace problematic characters (newlines, tabs)
        clean_text = clean_text.replace("\n", " ").replace("\r", " ").replace("\t", " ")
        return clean_text.strip()  
    
def get_weather(city="Kolkata"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"The temperature in {city} is {temp}°C with {desc}."
    else:
        return "Sorry, I couldn't fetch the weather right now."
    
def processCommand(c):
    if "shutdown" in c.lower():
        speak("Shutting down")
        time.sleep(1)
        print("Shutting down...")  
        exit(0)   # <-- immediately terminates the program
        
    if "launch calculator" in c.lower():
        os.system("start calc")
    elif "launch notepad" in c.lower():
        os.system("start notepad")
    elif "launch clock" in c.lower():
        os.system("start ms-clock:")
    elif "launch paint" in c.lower():
        os.system("start mspaint")
    elif "launch recycle bin" in c.lower():
        os.system("start shell:RecycleBinFolder")
    elif "launch file explorer" in c.lower():
        os.system("start explorer")
    elif "launch command prompt" in c.lower():
        os.system("start cmd")
    elif "launch powershell" in c.lower():
        os.system("start powershell")
    elif "launch photos" in c.lower():
        os.system("start ms-photos:")
    elif "launch one note" in c.lower():
        os.system("start onenote")
    elif "launch microsoft edge" in c.lower():
        os.system("start msedge")
    
    elif "take screenshot" in c.lower():
        speak("Taking screenshot")
        screenshot=pyautogui.screenshot()
        file_name=f"C:/Users/Parama Dey/OneDrive/画像/Screenshots/screenshot_{datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.png"
        screenshot.save(file_name)
        print(f"screenshot is taken and saved as: {file_name}")
        speak("the screenshot is taken and saved")
    
    elif "what time is it" in c.lower():
        strfTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strfTime}")
        print(f"The time is {strfTime}")
        
    elif "what date is it" in c.lower():
        strfDate = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {strfDate}")
        print(f"Today is {strfDate}")
        
    elif "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")
    elif "open colab" in c.lower():
        webbrowser.open("https://colab.research.google.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")  
          
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)

    elif "weather" in c.lower():
        # Default city or extract from command
        if "in" in c.lower():
            city = c.lower().split("in")[-1].strip()
        else:
            city = "Kolkata"  # default city
        weather_report = get_weather(city)
        print(weather_report)
        speak(weather_report)
        
    elif "news" in command.lower():
        response = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
        )
        if response.status_code == 200:
            print("Showing headlines...")
            data = response.json()
            Headline_list=[]
            for item in data["articles"]:
                headline = item.get("title", "")
                Headline_list.append(safe_speak(headline))
            combined_headlines=". Next headline: ".join(Headline_list)
            speak(combined_headlines)
            print(combined_headlines)
        else:
            print("Sorry, fail to fetch news")
            
    else:
        #let open ai handle the request
        output=aiProcess(c)
        speak(output)
        
def record_audio(duration=4, fs=16000):
    """Record audio using sounddevice and return an AudioData object for speech_recognition"""
    print("Listening...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    # Convert numpy array to AudioData
    return sr.AudioData(audio.tobytes(), fs, 2)

if __name__=="__main__":
    speak("Initializing Jarvis....")
    while True:
           
        try:
            print("recognizing...")
            audio=record_audio(duration=4)
            word=r.recognize_google(audio)
            print("Heard:",word)
            if word.lower()=="jarvis":
                engine.say("yeah")
                
                print("Wake word detected: Jarvis")
                #listen for command
                audio=record_audio(duration=5)
                command=r.recognize_google(audio)
                print("Command:",command)
                processCommand(command)
                
            elif word.lower() == "shutdown":
                
                speak("Shutting down")
                time.sleep(2)
                print("Shutting down...")
                break

        except sr.WaitTimeoutError:
            print("Sorry, I didn't hear anything")
        except sr.UnknownValueError:
            print("Can't understand the audio")
        except sr.RequestError as e:
            print(f"Error: {e}")
        