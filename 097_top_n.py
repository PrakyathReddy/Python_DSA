"""
There's a dictionary that lists a bunch of errors and their frequency. Need to order the error:frequency pairs based on frequency. Extract and produce the number of top pairs that the executor requests. 

what if any counts are equal - should I give preference based on alphabetical order of keys?

Create a new list based on value of each key sorted in descending order. Iterate through the loop to create a new dictionary with the number of top n items required.
"""

def top_n(data,number):
    sorted_list = sorted(data.values(), reverse=True) # only contains values of data for reference before producing top_n
    top_list = []
    counter = 0
    while counter < number: #
        for error, count in data.items():
            if count == sorted_list[counter]:
                key_value_couple = (error,count)
                top_list.append(key_value_couple)
        counter += 1
    return top_list

error_counts = {"TimeoutError": 45, "ConnectionRefused": 12, "OOMKilled": 78, "CrashLoopBackOff": 34, "ImagePullBackOff": 5}
print(top_n(error_counts, 3))