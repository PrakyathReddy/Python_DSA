"""
There's a list of numbers. Produce the max value adding 'n' number of any consecutive terms.

I'm assuming it'll only have positive integers and k will always be less than length of the list. Also, does the cycle end with the last 3 numbers or should it continue a little like a circle, as in last number + first + second number ?

Use slicing based on value of 'k' to produce multiple lists. For each list, produce sum and add to a list. Return max value of list. 
"""

def max_sum_subarray(nums, k):
    i = 0
    list = [] # list of lists containing numbers of a group in the sliding window
    while i <= (len(nums)-k):
        list.append(nums[i:k+i])
        i+=1
    j=0
    max_num_list = []
    while j < len(list):
        max_num_list.append(sum(list[j]))
        j+=1
    return max(max_num_list)

nums = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(nums,k))
# Output: 9  (because 5 + 1 + 3 = 9)