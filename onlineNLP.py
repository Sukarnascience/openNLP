# gemini_chatbot.py

from dotenv import load_dotenv
import os
import google.generativeai as genai
import requests

class GeminiChatbot:
    def __init__(self):
        print("""Hi! This is Sukarna Jana, the creator of this code.
Just a friendly reminder to create a .env file and set your GOOGLE_API_KEY environment variable before using this program.
Thank you!
================= Happy Chatting =================""")
        """
        Initialize the GeminiChatbot instance.
        """
        load_dotenv()  # Load environment variables from .env file
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            print("Invalid/No API Key in .env file")
            return

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-pro")
        self.chat = self.model.start_chat(history=[])

    def check_internet_connection(self):
        """
        Check if the internet connection is available.

        Returns:
        - bool: True if the internet is available, False otherwise.
        """
        try:
            requests.get("https://www.google.com", timeout=1)
            return True
        except requests.ConnectionError:
            return False

    def get_gemini_response(self, question):
        """
        Get response from the Gemini LLM model for the given question.

        Parameters:
        - question (str): The question to ask the Gemini LLM model.

        Returns:
        - list: The response from the Gemini LLM model or an error message if there is no internet.
        """
        if not self.check_internet_connection():
            return ["Sorry, can't connect to the internet. Please check your connection."]

        response = self.chat.send_message(question, stream=True)
        return [chunk.text for chunk in response]


# Example usage:
#chatbot = GeminiChatbot()
#input_text = "Do You know about lord Sri Krishna"
#response = chatbot.get_gemini_response(input_text)
#for chunk in response:
#    print(chunk)
