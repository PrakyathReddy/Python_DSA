with open('resources/access.log', 'r') as file:
    code_list = []
    for code in file:
        code_list.append(code.strip().split()[-1])
    for i in set(code_list):
        print(f"{i}: {code_list.count(i)}")
