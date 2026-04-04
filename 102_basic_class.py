"""
Create a class that accepts a list of server names, assigns health status randomly and adds to dictionary. Has another method called report to produce a list of servers that are unhealthy.

I'm assuming the list will contain only strings

Create class, initiate it with list. Define a function that appends to a dictionary the server name with health status assigned randomly using random function. Create another function that iterates through the dictionary, and adds to another list that only contains servers that are unhealthy.
"""
import random

class HealthChecker:
    def __init__(self, server_list):
        self.server_list = server_list
    
    def check(self):
        self.server_status_pair = {}
        status = ["Healthy", "Unhealthy"]
        for item in self.server_list:
            self.server_status_pair[item] = random.choice(status)
        return self.server_status_pair

    def report(self):
        self.check() # in cases where check is not run before running report
        for item in self.server_status_pair:
            if self.server_status_pair[item] == "Unhealthy":
                print(f"{item} is Unhealthy")




checker = HealthChecker(["web-01", "db-01", "cache-01"])
# print(checker.check())
print(checker.report())
