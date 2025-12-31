**Jarvis**: Personal Desktop Assistant
A modular, voice-activated desktop assistant built with Python. 

🚀 **Features**
**Voice Control**: Uses SpeechRecognition and sounddevice for hands-free interaction.

**AI Brain**: Integrated with Google Gemini API for natural language processing and short, smart responses.

**System Automation:**

Launch Windows applications (Calculator, Notepad, File Explorer, etc.).

Take and save screenshots automatically.

Fetch current date and time.

**Web Integration:**

Quick links to Google, YouTube, LinkedIn, GitHub, and WhatsApp.

Music playback via a custom musicLibrary module.

**Real-time Info:**
Weather: Live weather updates for any city via OpenWeatherMap API.

News: Top headlines fetched via NewsAPI.

🛠️ **Tech Stack**
Language: Python 3.x

AI Model: Google Gemini 2.5 Flash

Libraries: * pyttsx3 (Text-to-Speech)

SpeechRecognition (Google Speech API)

PyAutoGUI (GUI Automation)

Requests (API calls)

Dotenv (Environment management)

📋 **Prerequisites**
Before running the project, ensure you have the following API keys:

Gemini API Key: Obtain from Google AI Studio.

OpenWeatherMap API Key: Obtain from OpenWeather.

NewsAPI Key: Obtain from NewsAPI.org.

🎙️ **Usage**
Run the main script: python main.py

Say the wake word "Jarvis".

Give a command, for example:

"Launch Notepad"

"weather"

"Play Faded"

"news"

"Take screenshot"

To exit the program, simply say "Shutdown".
