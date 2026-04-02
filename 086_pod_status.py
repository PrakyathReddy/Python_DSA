pods = [("nginx-7d4b", "Running"), ("redis-a3f1", "CrashLoopBackOff"), ("postgres-9c2e", "Running"), ("app-b8d5", "Error")]

for pod,status in pods:
    if status != "Running":
        print(f"Pod: {pod:<20}           Status: {status}")