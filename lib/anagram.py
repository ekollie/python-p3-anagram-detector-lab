import ipdb

class Anagram():

    def __init__(self, word):
        self.word = word

    def match(self, input_list):
        deconstructed_word = sorted([letter for letter in self.word])
        return [word for word in input_list if sorted([letter for letter in word]) == deconstructed_word]

# ipdb.set_trace()