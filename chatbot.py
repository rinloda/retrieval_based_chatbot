from collections import Counter
from sre_constants import CATEGORY
from user_functions import preprocess, compare_overlap, pos_tag, extract_nouns, compute_similarity
from responses import response_1, response_2, blank_spot
from not_match_intent import response_no_match
import spacy
import random

word2vec = spacy.load('en_core_web_md')

exit_commands = ("quit", "goodbye", "exit", "no")
responses = response_1 + response_2
class ChatBot:

    # Define .make_exit() below:
    def make_exit(self, user_message):
        # Check each word(exit command) in exit_commands list in condition if exit_command inside user_message
        # Print goodbye message and return True
        for exit_command in exit_commands:
            if exit_command in user_message:
                print("Alright, thank you for taking time with me. Have a good day!")
                return True
    
    # Define .chat() below:
    def chat(self):
        name = input("Welcome to Casa de Tan Bank, my name is Lucretia. \nMay I know your name\n")
        user_message = input('Hello {}, how can I help you? \n'.format(name))
        while not self.make_exit(user_message):
            user_message = self.respond(user_message)

    # Define .find_intent_match() below:
    def find_intent_match(self, responses, user_message):
        bow_user_message = Counter(preprocess(user_message))
        process_response = [Counter(preprocess(response)) for response in responses]
        similarity_list = [compare_overlap(doc, user_message) for doc in process_response] 
        response_index = similarity_list.index(max(similarity_list))
        return responses[response_index]

    # Define .find_entities() below
    def find_entiities(self, user_message):
        tagged_user_message = pos_tag(preprocess(user_message))
        message_nouns = extract_nouns(tagged_user_message)
        tokens = word2vec(" ".join(message_nouns))
        category = word2vec(blank_spot)
        word2vec_result = compute_similarity(tokens, category)
        word2vec_result.sort(key=lambda x: x[2])
        if len(word2vec_result) < 1:
            return blank_spot
        else: return word2vec_result[-1][0]

    # Define .respond() below
    def respond(self, user_message):
        best_response = self.find_intent_match(responses, user_message)
        entity = self.find_entiities(user_message)
        print(best_response.format(entity))
        return best_response.format(entity)
        # input_message = input("How else can I help you?.\n")
        # return input_message

    def other_message(self, user_message):
        user_message = input("How else can I help you?.\n")
        return user_message

    def no_match_inten(self):
        reply = response_no_match
        return random.choice(reply)
        
# initalize ChatBot instance below
Lucretia = ChatBot()
#Lucretia.chat() 