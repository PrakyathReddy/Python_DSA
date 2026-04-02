server_status = {"web01":"Healthy", "web02":"Unhealthy", "web03": "Healthy"}

for server in server_status.keys():
    print(server + " is " + server_status[server])