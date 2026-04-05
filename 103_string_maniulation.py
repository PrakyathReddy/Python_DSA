"""
Accept 2 strings. Check if they are anagrams or not

Can I use sort or need to do without it ? Does case matter ?

accept 2 strings. sort them both. if equivalent, return True else False
"""
def is_anagram(str1, str2):
    sort_str1 = sorted(str1)
    sort_str2 = sorted(str2)
    return sort_str1 == sort_str2

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))   # False
print(is_anagram("node", "done"))     # True