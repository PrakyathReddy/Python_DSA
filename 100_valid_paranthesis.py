"""
There are 3 types of brackets {},[],(). They are arranged in random and different combitions of them are passed as input. The function should evaluate the patterns and identify if they are valid - valid means open and closed brackets beside each other, and in the same order.

Do you want it to be extensible ? as in more types of brackets can be added in future or maybe some can be removed.

Anything that opens should close too. Use a stack / list to add items as you iterate through the string. if a closing bracket is encountered, delete the corresponding opening bracket from the stack. After iterating through the string, if list is empty, string is valid, else invalid. 
"""
def valid_paranthesis(string):
    list = [] # stack LIFO
    dictionary = { "}":"{", "]":"[", ")":"(" }
    for char in string:
        if char in [ "{", "(", "[" ]:
            list.append(char)
        if char in [ "}", ")", "]" ]:
            if list.pop() != dictionary[char]:
                return False
    return len(list) == 0


pattern = "[]{()}"
pattern2 = "{[}]()"
print(valid_paranthesis(pattern))
print(valid_paranthesis(pattern2))