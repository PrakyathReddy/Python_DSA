server_status = {"Web01": "Healthy", "Web02": "Unhealthy", "Web03": "Unhealthy", "Web04": "Healthy", "Web05": "Unhealthy", }

count=0
for server, status in server_status.items():
    if status == "Unhealthy":
        print(f"{server} is {status}")
        count+=1

print(f"{count} servers are unhealthy")

