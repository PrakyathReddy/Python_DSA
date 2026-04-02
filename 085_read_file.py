server_health = {}
with open('resources/servers.txt','r') as file:
    for line in file:
        server, status = line.strip().split(",")
        server_health[server] = status

print(server_health)