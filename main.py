import requests
import offlineNLP as offchatbot
import onlineNLP as onchatbot

import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import pygame

import re

hotKey = "robot"
speed = 150

def remove_special_chars(text):
    special_chars = '()[]!*\n^'
    filtered_text = ''.join(char for char in text if char not in special_chars)
    return filtered_text

def convert_text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to convert text to speech
def Google_text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language)
    audio_path = 'output.mp3'
    tts.save(audio_path)

    pygame.mixer.init()
    sound = pygame.mixer.Sound(audio_path)
    sound.play()
    pygame.time.wait(int(sound.get_length()) * 1000)

def is_internet_available():
    try:
        # Try to make a request to a well-known website
        response = requests.get("http://www.google.com", timeout=5)
        # If the status code is 200, internet is available
        return response.status_code == 200
    except requests.ConnectionError:
        # If there's a connection error, internet is not available
        return False


def chatBotONLINE():
    def listen_and_respond():
        # Initialize the speech recognition and text-to-speech engines
        recognizer = sr.Recognizer()
        engine = pyttsx3.init()
        engine.setProperty('rate', speed)

        # Start listening for activation keyword
        while True:
            with sr.Microphone() as source:
                print("Listening for activation keyword...")
                recognizer.pause_threshold = 1
                audio = recognizer.listen(source)

            try:
                # Use speech recognition to convert speech to text
                activation_keyword = recognizer.recognize_google(audio).lower()
                print("Activation Keyword : ", activation_keyword)

                if hotKey in activation_keyword:
                    Google_text_to_speech("Hello! How can I assist you?")
                    #engine.say("Hello! How can I assist you?")
                    #engine.runAndWait()

                    # Listen for commands until stop keyword is said
                    while True:
                        with sr.Microphone() as source:
                            print("Listening for commands...")
                            recognizer.pause_threshold = 1
                            audio = recognizer.listen(source)

                        try:
                            command = recognizer.recognize_google(audio).lower()
                            print("Command:", command)
                            response = online_chatbot.get_gemini_response(command)
                            print("Gimini : ",response)

                            # Fixed the Output Properly
                            plain_text_response = [remove_special_chars(text) for text in response]
                            # Merge into one long text
                            merged_text = ' '.join(plain_text_response)
                            print("Reframe : ",merged_text)

                            Google_text_to_speech(merged_text)
                            #engine.say(merged_text)
                            #engine.runAndWait()

                            if "stop" in command:
                                Google_text_to_speech("Goodbye!")
                                #engine.say("Goodbye!")
                                #engine.runAndWait()
                                break  # Exit the inner loop and stop listening for commands

                            # Add your custom logic to handle different commands here
                            # ...

                        except sr.UnknownValueError:
                            print("Sorry, I didn't understand that.")

            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")

    # Start the voice-activated assistant
    listen_and_respond()


def chatBotOFFLINE():
    while True:
        input_text = input("You: ")
        if(input_text.lower() == "shutdown"):
            break 
        response = offline_chatbot.get_response(input_text)
        print("Bot:", response)


if __name__ == '__main__':
    if is_internet_available():
        online_chatbot = onchatbot.GeminiChatbot()
        chatBotONLINE()
    else:
        # Its not fully offline still it use internet to convert Speech to Text
        print("Its not fully offline still it use internet to convert Speech to Text")
        offline_chatbot = offchatbot.Chatbot()
        chatBotOFFLINE()
