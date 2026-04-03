def find_duplicates(data):
    count = {} # to store the number of times a piece of data occurs
    for item in data:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    duplicates = []
    for item in count:
        if count[item] > 1:
            duplicates.append(item)
    return duplicates

data = ["pod-a", "pod-b", "pod-c", "pod-a", "pod-d", "pod-b"]
print(find_duplicates(data))