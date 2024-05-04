# Intelligent Digital Assistant (IDA) - Speech Recognition Project

## Overview
IDA (Intelligent Digital Assistant) is a Python-based personal assistant that utilizes speech recognition and synthesis to perform various tasks upon voice commands. This project aims to provide users with a hands-free interaction experience, enabling them to execute commands, retrieve information, and perform actions using voice input.

## Features
- **Voice Recognition:** Utilizes the `speech_recognition` library to convert speech input into text.
- **Voice Synthesis:** Employs the `pyttsx3` library for text-to-speech conversion, enabling IDA to respond audibly to user commands.
- **Basic Task Automation:** Executes tasks such as opening web browsers, applications, retrieving information from Wikipedia, playing music on YouTube, fetching news headlines, etc.
- **Customizable Responses:** Allows for customization of voice responses and greetings based on the time of day.
- **Multi-functionality:** Capable of performing various tasks like fetching weather information, telling jokes, searching the web, etc.

## Prerequisites
- Python 3.x
- Internet connection (for some functionalities like fetching Wikipedia data, news headlines, weather information, etc.)

## Installation
1. Clone or download the project repository.
2. Install the required Python libraries using pip:
    ```
    pip install -r requirements.txt
    ```
3. Run the `ida.py` script to start the IDA personal assistant.

## Requirements
The following libraries are required to run IDA:
speechrecognition==3.8.1
pyttsx3==2.90
wikipedia==1.4.0
pywhatkit==5.1
pyjokes==0.6.0


## Usage
1. Run the `ida.py` script in your Python environment.
2. Upon execution, IDA will greet you based on the time of day (Good Morning/Afternoon/Evening).
3. IDA will then listen for your voice commands.
4. Speak your command clearly, and IDA will execute the corresponding action or provide a response.
5. You can ask IDA to perform tasks like opening websites, fetching information from Wikipedia, playing music on YouTube, etc.
6. To exit the IDA application, simply say "Goodbye" or "Stop".

## Supported Commands
- Open YouTube/Google/Gmail
- Search Wikipedia
- Fetch news headlines
- Play music on YouTube
- Tell a joke
- Fetch weather information
- Open applications like Notepad, Word, etc.
- Log off/sign out of the system

## Contributions
Contributions to enhance the functionality, add new features, or improve the existing codebase are welcome. Feel free to fork the repository, make your changes, and submit a pull request.

## Credits
- This project was developed by Mathusoothanan k.
- Special thanks to the developers of the libraries used in this project.

