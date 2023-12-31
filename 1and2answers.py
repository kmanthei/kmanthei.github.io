import re
from collections import defaultdict

#Questions 1 & 2

requests_per_day = defaultdict(int)
requests_per_week = defaultdict(int)
requests_per_month = defaultdict(int)

# Change log path to go to where your file is logatdd)
log_file_path = "/Users/egrace/Downloads/logfile.txt"

#This will open the log file and assign it a variable as log_file
#With this loop if the log file is not found, then it will return a message letting the user know to check the location

try:
    with open(log_file_path, 'r') as log_file:
        log_data = log_file.readlines()
except FileNotFoundError:
    print(f"File '{log_file_path}' not found. Make sure the file exists in the correct location.")
    exit()

#this is assigning the data_pattern variable to the function that is called compile regex pattern
#this will search for the specified pattern
date_pattern = re.compile(r'\[(\d{2}/\w+/\d{4}):')

for log_entry in log_data:
    match = date_pattern.search(log_entry)
    if match:
        date = match.group(1)

#this will split the day, month, and year wherever the backslash is        
        day, month, year = date.split('/')
        week_number = f"{year}-{month}-{day}"
        month_year = f"{year}-{month}"

        
        requests_per_day[date] += 1
        requests_per_week[week_number] += 1
        requests_per_month[month_year] += 1

# Shows the answer for questions 1 and 2
print("Requests per day:")
for date, count in requests_per_day.items():
    print(f"{date}: {count}")

print("\nRequests per week:")
for week, count in requests_per_week.items():
    print(f"Week {week}: {count}")

print("\nRequests per month:")
for month, count in requests_per_month.items():
    print(f"{month}: {count}")
