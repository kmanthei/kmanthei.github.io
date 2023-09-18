import os
import re
from datetime import datetime

os.chdir('/Users/willh/Downloads/')

input_log_file = 'logfile.txt'
output_directory = 'logs_by_month'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

month_files = {}

with open(input_log_file, 'r') as input_file:
    for line in input_file:
        timestamp_match = re.search(r'\[(.*?)\]', line)
        
        if timestamp_match:
            timestamp_str = timestamp_match.group(1)
            log_date = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S %z')
            
            month_year = log_date.strftime('%Y-%m')
            
            if month_year not in month_files:
                month_file_path = os.path.join(output_directory, f'log_{month_year}.txt')
                month_files[month_year] = open(month_file_path, 'a')
            
            month_files[month_year].write(line)

for file in month_files.values():
    file.close()
