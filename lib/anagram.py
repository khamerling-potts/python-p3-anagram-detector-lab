# your code goes here!
class Anagram:
    def __init__(self, anagram):
        self.anagram = anagram

    def match(self, list):
        matches = []
        target = [char for char in self.anagram]

        for word in list:
            potential_match = [char for char in word]
            if sorted(potential_match) == sorted(target):
                matches.append(word)

        return matches
