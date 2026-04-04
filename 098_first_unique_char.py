"""
Letters in a word are repeating most of time. Find the first one that doesn't.

Can I assume it won't have any spaces ? 

Iterate through the word, create a dictionary that shows the count of each letter. Iterate through the dictionary, the first character with 1 as the value should be returned. None if no such value.
"""

def first_unique_char(word):
    count = {}

    for letter in word:
        if letter in count:
            count[letter] += 1
        else: 
            count[letter] = 1

    for letter in word: # iterating through word and not count since dictionary need not be ordered in some versions of python
        if count[letter] == 1:
            return letter # it handles none case too since if the loop finishes wihout a character, it returns None anyways


string = "aabbcdd"
print(first_unique_char(string))