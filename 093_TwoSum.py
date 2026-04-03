def TwoSum(numbers):
    list = []
    for i in numbers:
        for j in numbers:
            if (i+j) == 9:
                list.append(numbers.index(i))
    return list

nums = [2, 7, 11, 15]
print(TwoSum(nums))