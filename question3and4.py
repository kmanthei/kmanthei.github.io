import os
os.chdir('/Users/kailimanthei/Downloads')

#opening the log file from personal directory
original_log_file = 'log.txt'

#status code 4xx involves bad request, unauthorized, forbidden, and not found, here we are setting the range for python to look for which is 400-499
unsuccessful_status_codes = [str(code) for code in range(400, 499)]

#here we are creating the variables
total_requests = 0
unsuccessful_requests = 0

#this will open the original file and begin reading and sorting through it 
with open(original_log_file, 'r') as log_file:
    for line in log_file:
        try:
            status_code = int(line.split()[2])  
            total_requests += 1

            
            #this checks if it is in the 4xx range of being unsuccesful 
            if str(status_code) in unsuccessful_status_codes:
                unsuccessful_requests += 1
        except (IndexError, ValueError):
            pass

# this will turn the decimal answer into a percentage by dividing the unsuccessful requests by total requests and multiplying by 100
if total_requests > 0:
    unsuccessful_percentage = (unsuccessful_requests / total_requests) * 100
else:
    unsuccessful_percentage = 0.0  

print(f"The percentage of unsuccessful requests (4xx status codes) is: {unsuccessful_percentage:.2f}%")







# this is referring to the log file that is downloaded on my laptop
original_log_file = 'log.txt'

# this is the range for redirection meaning it was moved permanently, found, or not modified
redirection_status_codes = [str(code) for code in range(300, 399)]

# these are the variables we will use within the loops 
total_requests = 0
redirected_requests = 0

# this will open the log file and read it 
with open(original_log_file, 'r') as log_file:
    for line in log_file:
        try:
            status_code = int(line.split()[2])  
            total_requests += 1
            
            # this will check if the status code is within 300-399
            if str(status_code) in redirection_status_codes:
                redirected_requests += 1
        except (IndexError, ValueError):
            pass

# this turns the decimal into a percentage by dividing the redirected requests by total and multiplying by 100
if total_requests > 0:
    redirection_percentage = (redirected_requests / total_requests) * 100
else:
    redirection_percentage = 0.0  

print(f"The percentage of redirected requests (3xx status codes) is: {redirection_percentage:.2f}%")
