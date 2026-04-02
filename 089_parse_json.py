import json

with open('resources/pods.json') as json_file:
    logs = json.load(json_file)
    for details in logs:
        if details["status"] != "Running":
            print(f'{details["name"]} | {details["status"]} | {details["restarts"]}')
