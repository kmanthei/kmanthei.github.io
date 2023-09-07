import re
from datetime import datetime, timezone
import os

os.chdir('/Users/willh/Downloads/')
log_file_path = "logfile.txt"

def parse_log_file():
    try:
        with open(log_file_path, "r") as file:
            log_data = file.readlines()

        total_requests = len(log_data)

        log_entry_pattern = r'\S+ \S+ \S+ \[([\w:/]+\s[+\-]\d{4})\] "[A-Z]+ (.+?) HTTP/\d\.\d" \d+ \d+'

        start_date = datetime.strptime("Mar 1 00:00:00 1995", "%b %d %H:%M:%S %Y").replace(tzinfo=timezone.utc)
        end_date = datetime.strptime("Aug 31 23:59:59 1995", "%b %d %H:%M:%S %Y").replace(tzinfo=timezone.utc)

        requests_in_range = 0

        for entry in log_data:
            match = re.match(log_entry_pattern, entry)
            if match:
                log_date = datetime.strptime(match.group(1), "%d/%b/%Y:%H:%M:%S %z")
                if start_date <= log_date <= end_date:
                    requests_in_range += 1

        print("Total requests in the 6-month period:", requests_in_range)
        print("Total requests in the log:", total_requests)
    
    except FileNotFoundError:
        print("Log file not found. Please make sure the file exists at:", log_file_path)

parse_log_file()
