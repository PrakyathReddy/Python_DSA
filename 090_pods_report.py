import json

with open('resources/pods.json') as file:
    pod_dict = json.load(file)

def pod_report(pod_dict):
        summary = {}
        summary["total"] = len(pod_dict)
        summary["healthy"] = 0
        summary["unhealthy"] = 0
        pod_names = []

        for details in pod_dict:
            if details["status"] == "Running":
                summary["healthy"] += 1
            elif details["status"] != "Running":
                summary["unhealthy"] += 1
            if details["restarts"] > 5:
                pod_names.append(details["name"])

        summary["high_restarts"] = pod_names
        return summary

print(pod_report(pod_dict))