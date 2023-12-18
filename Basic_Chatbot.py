import nltk
import random
import re
from nltk.chat.util import Chat, reflections

bot_responses = [
    (r"hi|hello", ["Hello!", "Hi there!"]),
    (r"how are you", ["I'm doing well, thank you."]),
    (r"what's your name", ["I'm just a humble chatbot."]),
    (r"bye", ["Goodbye!", "See you later!"]),
    (r"(.*)", ["Sorry, I'm not sure I understand."]),
]

class SimpleChatBot(Chat):
    def __init__(self, pairs, reflections={}):
        super().__init__(pairs, reflections)
    
    def respond(self, input_message):
        response = None
        for pattern, responses in self._pairs:
            if re.match(pattern, input_message):
                response = random.choice(responses)
                break
        return response if response else random.choice(self._reflections["default"])
simple_bot = SimpleChatBot(bot_responses, reflections)
print("Bot: Hi there! How can I help you today?")
while True:
    user_input = input("You: ")
    response = simple_bot.respond(user_input)
    print("Bot:", response)
    if user_input.lower() == 'bye':
        break
