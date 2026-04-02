server_status = {"web01":"Healthy", "web02":"Unhealthy", "web03": "Healthy"}

for server in server_status:
    print(f"{server} is {server_status[server]}")

for server, status in server_status.items():
    print(f"{server} is {status}")