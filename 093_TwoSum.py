# def TwoSum(numbers):
#     list = []
#     for i in numbers:
#         for j in numbers:
#             if (i+j) == 9:
#                 list.append(numbers.index(i))
#     return list

# nums = [2, 7, 11, 15]
# print(TwoSum(nums))

def TwoSum(numbers, target):
    seen = {} # map number to it's index using enumerate
    for index, value in enumerate(numbers):
        complement = target - value
        # print(f"index: {index}, value: {value}, complement: {complement}")
        # print(f"check seen: {seen}")
        # print(f"check seen before: {complement in seen.values()}")
        if complement in seen:
            return [seen[complement],index]    
        seen[value] = index    

nums = [2, 7, 11, 15]
target = 9
print(TwoSum(nums,target))