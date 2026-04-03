def group_by_status(data):
    status_of_pods = {}
    for pod, status in data:
        if status in status_of_pods:
            status_of_pods[status].append(pod)
        else:
            status_of_pods[status] = [pod]
    return status_of_pods


pods = [
    ("nginx", "Running"),
    ("redis", "Failed"),
    ("postgres", "Running"),
    ("app", "Pending"),
    ("worker", "Failed"),
    ("cache", "Running")
]
print(group_by_status(pods))

some_other_pods = [ ("k8s", "Running"), ("containers", "OOM") ]
print(group_by_status(some_other_pods))