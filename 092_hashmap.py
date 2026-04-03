def count_occurences(overall_list):
    count_recurrence = {}
    for item in overall_list:
        if item in count_recurrence:
            count_recurrence[item] += 1
        else:
            count_recurrence[item] = 1
    
    return count_recurrence

logs = ["error", "warning", "error", "info", "error", "warning", "info", "info", "info", "error"]
print(count_occurences(logs))
