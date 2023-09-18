#Provides a way to provide the platform
import os
 
#This is the directory where the files are located 
os.chdir('/Users/willh/Downloads/')

# Irene's Directory to find the path 
# Questions 5 and 6
os.chdir ('/Users/irene/Downloads/ITSV 412/Project #3- Using Python/')

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

# This is the code to answer Group Project #4 Log Parsing in Python Part 2
# Answer for questions 5 and 6 
	
from collections import Counter

# Read file directly into a Counter
with open('3.1 Four dimensions of service management.txt') as f:
    cnts = Counter(l.strip() for l in f)

# Display 3 most common lines
cnts.requested(1)

# Display 3 least common lines
cnts.requested()[-1:]


#This will show the amount it finds in the code 
# Programming in python  assignment
print("The total length is:", total_requests)
print("The total length in the past six months is:", six_months)

# Answer for questions 5 and 6 on Group Project #4 Log Paarsing in Python Part 2
print(" the least requested list is:", cnts.requested(1))
print(" the most requested list it:", cnts.requested()[-1:])







     
   
   

