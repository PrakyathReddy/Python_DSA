import importlib

pods_report = importlib.import_module("090_pods_report")

with open('resources/pods.json','r') as file:
    pod_dictionary = json.load(file)
    pod_report(pod_dictionary)
