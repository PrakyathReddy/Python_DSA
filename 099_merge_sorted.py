"""
accepts 2 sorted lists and returns a combined sorted list without using sorted(), rather combine them comparing the elements in both lists

should i take negative numbers into consideration too ? Can I assume it wouldn't contain strings, complex numbers, fractions, decimals, etc. ?

grab the smallest element from list_a, and smallest from list_b, compare them. Add the smallest to the new list and pop same from original one. Now repeat the comparision to populate the new list.
"""
def merge_sorted(list1, list2):
    sorted_list = []
    i=0
    j=0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            sorted_list.append(list1[i])
            i+=1
        else:
            sorted_list.append(list2[j])
            j+=1

    if i == len(list1):
        sorted_list.extend(list2[j:])
    elif j == len(list2):
            sorted_list.extend(list1[i:])

    return sorted_list

list_a = [1, 3, 5, 7, 9]
list_b = [2, 4, 6, 8, 10, 12, 14, 16]
print(merge_sorted(list_a, list_b))
# Output: [1, 2, 3, 4, 5, 6, 7, 8]