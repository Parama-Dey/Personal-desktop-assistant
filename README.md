## Jarvis – Voice Controlled AI Assistant 🎙️🤖
Jarvis is a Python-based voice assistant that can recognize speech, respond with voice feedback, launch Windows applications, fetch weather updates, read news headlines, play music, and even interact with Google Gemini AI for intelligent responses.

## ✨ Features
**Wake word detection:** Activate Jarvis by saying "Jarvis".

**Speech recognition:** Uses Google Speech Recognition to process voice commands.

**Voice feedback:** Speaks responses using pyttsx3.

**AI integration:** Connects to Google Gemini API for conversational replies.

**Weather updates:** Fetches real-time weather using OpenWeather API.

**News headlines:** Reads top US headlines via NewsAPI.

**Windows automation:** Launches apps like Calculator, Notepad, Paint, Edge, etc.

**Web browsing:** Opens Google, YouTube, LinkedIn, GitHub, WhatsApp Web, Colab.

**Music playback:** Plays songs from a custom musicLibrary.

**Screenshot capture:** Takes and saves screenshots automatically.

**Date & time reporting:** Speaks current time and date.

**Shutdown command:** Terminates the assistant safely.

## 🛠️ Requirements
**Install the following Python packages:**

bash
pip install speechrecognition sounddevice pyttsx3 requests python-dotenv pyautogui
**Additional dependencies:**

**musicLibrary.py:** A custom dictionary mapping song names to URLs.

**Google Speech Recognition:** Requires internet connection.

**Windows OS:** For app launching and automation.

## 🔑 Environment Variables
Create a .env file in the project root with the following keys:

**GEMINI_API_KEY**=your_gemini_api_key_here
**WEATHER_API_KEY**=your_openweather_api_key_here
**NEWS_API_KEY**=your_newsapi_key_here
## 📂 Project Structure
Jarvis/
│── jarvis.py          # Main assistant script
│── musicLibrary.py    # Dictionary of songs and links
│── .env               # API keys
## ▶️ Usage
**Run the assistant:**

bash
python jarvis.py
Say "Jarvis" to wake the assistant.

Give commands like:

"Launch calculator"

"Open YouTube"

"Play Alone"

"What time is it?"

"Weather in Kolkata"

"News"

"Shutdown"

## ⚠️ Notes
Works best on Windows (due to os.system app launch commands).

Requires internet connection for AI, weather, news, and speech recognition.

Screenshot path is hardcoded; update it to your preferred directory.

## 🚀 Future Improvements
Add support for more apps and services.

Enhance error handling and offline capabilities.

Modularize commands for easier expansion.
