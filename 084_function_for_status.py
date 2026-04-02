server_statuss = {"Web01": "Healthy", "Web02": "Unhealthy", "Web03": "Unhealthy", "Web04": "Healthy", "Web05": "Unhealthy", }

def check_servers(dictionary):
    server_list = []
    for server, status in dictionary.items():
        if status == "Unhealthy":
            server_list.append(server)
    return server_list


print(check_servers(server_statuss))