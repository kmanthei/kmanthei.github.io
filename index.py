#Provides a way to provide the platform
import os
 
#This is the directory where the files are located 
os.chdir('/Users/willh/Downloads/')

# This is going to go through the file and find the lines that have the request
# Code for the total requests
try:
    total_requests = 0
    with open("logfile.txt", "r") as file:
        for line in file:
            total_requests += 1
# If not found an error message will show
except FileNotFoundError:
    print("Please check the path.")
 
# This is going to go through the file and find the lines that have the request
# Code for the last six months 
try: 
	six_months = 0
	with open("3.1 Four dimensions of service management.txt", "r") as file:
		for line in line:
				six_months = total_requests/2
# If not found an error message will show    		
except FileNotFoundError:
    print("Please check the path.")
    

#This will show the the amount it finds in the code    
print("The total length is:", total_requests)
print("The total length in the past six months is:", six_months)
