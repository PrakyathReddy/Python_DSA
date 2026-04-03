def reverse_string(word):
    reversed_string = ""
    counter = len(word) - 1 # using this as reference to reverse the string
    while counter >= 0:
        reversed_string += word[counter]
        counter -= 1
    return reversed_string

word = "kubernetes"
print(reverse_string(word))