import aiml

class Chatbot:
    def __init__(self):

        print("""Hi! This is Sukarna Jana, the creator of this code.
Its a offline Mode which was trained long back.
Thank you!
================= Happy Chatting =================""")

        self.kernel = aiml.Kernel()
        self.kernel.learn("std-startup.xml")
        self.kernel.respond("LOAD AIML B")

    def get_response(self, input_text):
        """
        Get response based on the input text.

        Parameters:
        - input_text (str): The input text.

        Returns:
        - str: The response from the chatbot.
        """
        return self.kernel.respond(input_text)

# Example usage:
#chatbot = Chatbot()
#input_text = input("You: ")
#response = chatbot.get_response(input_text)
#print("Bot:", response)
