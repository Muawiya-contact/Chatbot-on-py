import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

class BasicChatbot:
    """
    A basic text-based chatbot built using NLTK library.
    This chatbot can have simple conversations based on predefined patterns.
    """

    def __init__(self):
        """
        Initializes the chatbot with a set of predefined conversation patterns.
        """
        self.pairs = [
            (r"hi|hello|hey", ["Hello! How can I assist you today?"]),
            (r"how are you?", ["I'm just a bot, but I'm doing fine. How about you?"]),
            (r"what is your name?", ["I'm a chatbot created by Muawiya."]),
            (r"what can you do?", ["I can assist you with basic questions and carry out simple conversations."]),
            (r"bye|goodbye", ["Goodbye! Have a great day!"]),
            (r"(.*)", ["I'm sorry, I didn't understand that. Can you ask something else?"])
            (r"how old are you?", ["I don't age like humans, but I was created recently!"]),
            (r"tell me a joke", ["Why don't skeletons fight each other? They don't have the guts!"]),
            (r"what is your favorite color?", ["I don't have preferences, but I think blue is a nice color."]),
            (r"what can you help me with?", ["I can help you with answering questions, playing games, or even just chatting!"]),
            (r"where are you from?", ["I was created by Muawiya, so you could say I'm from the world of code!"]),
            (r"what is the meaning of life?", ["That's a philosophical question! Some say the meaning is to find happiness, others say it's 42."]),
            (r"do you know any fun facts?", ["Did you know? The longest word in the English language has 189,819 letters!"]),
            (r"can you help me with programming?", ["Yes! I can assist you with programming questions or problems. Just ask!"]),
            (r"who is the president of the united states?", ["The current president of the United States is Joe Biden."]),
            (r"what is the weather like?", ["I don't have real-time data access, but you can check a weather website or app for the latest updates!"]),
            (r"do you have emotions?", ["I don't have emotions like humans, but I'm here to help you as best as I can!"]),
            (r"can you sing?", ["I can't sing, but I can tell you the lyrics to your favorite song!"]),
            (r"tell me a fact about space", ["Did you know that the Sun makes up 99.86% of the mass in our solar system?"]),
            (r"how do you work?", ["I work by analyzing patterns in the text you type and matching them to my database of predefined responses."]),
            (r"what do you like to do?", ["I enjoy answering your questions and engaging in fun conversations!"]),
            (r"can you translate?", ["I can help with simple translations. What do you need translated?"]),
            (r"what is 2 plus 2?", ["2 plus 2 is 4!"]),
            (r"what time is it?", ["I can't check the time right now, but you can look at your device's clock for the current time."]),
            (r"tell me a riddle", ["What has keys but can't open locks? A piano!"]),
            (r"how can I improve my coding skills?", ["Practice is key! Try solving coding challenges and building projects to improve."]),
            (r"can you tell me about artificial intelligence?", ["Artificial Intelligence (AI) refers to machines or software that can perform tasks that usually require human intelligence, like problem-solving and learning."]),
            (r"who is your creator?", ["I was created by Muawiya, a talented developer and enthusiast of programming."]),
            (r"what do you think about humans?", ["Humans are fascinating creatures! You have creativity, emotions, and complex reasoning abilities."]),
            (r"what is your favorite food?", ["I don't eat, but if I could, I'd probably enjoy some byte-sized data!"]),
            (r"do you have any hobbies?", ["I enjoy chatting with users like you!"]),
            (r"what is your purpose?", ["My purpose is to assist you with information and engage in conversations."]),
        ]
        # Initialize the Chat class with the predefined conversation pairs and reflections
        self.chatbot = Chat(self.pairs, reflections)

    def start_conversation(self):
        """
        Starts an interactive conversation with the chatbot.
        The conversation continues until the user types 'quit'.
        """
        print("Hello! I am a Chatbot. Type 'quit' to end the conversation.")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                # Exit the conversation if user types 'quit'
                if user_input.lower() == 'quit':
                    print("Chatbot: Goodbye! Take care!")
                    break

                # Get the chatbot's response
                response = self.chatbot.respond(user_input)
                
                # Handle case where no response was found
                if response is None:
                    print("Chatbot: I'm sorry, I didn't understand that. Can you try rephrasing?")
                else:
                    print(f"Chatbot: {response}")
            
            except KeyboardInterrupt:
                print("\nChatbot: Goodbye! Take care!")
                break
            except Exception as e:
                print(f"Error: {e}")
                break

if __name__ == "__main__":
    # Create an instance of the chatbot and start the conversation
    bot = BasicChatbot()
    bot.start_conversation()
