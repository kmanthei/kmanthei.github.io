import os

os.chdir('/Users/willh/Downloads/')

try:
    total_requests = 0
    with open("logfile.txt", "r") as file:
        for line in file:
            total_requests += 1
except FileNotFoundError:
    print("Please check the path.")
    
print("The total length is:", total_requests)
print("The total length in the past six months is:", )
