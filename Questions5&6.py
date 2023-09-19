
#Group Project #4 Log Parsing in Python Part 2 
import os

# Change directory to file to your path 
os.chdir ('/Users/irene/Downloads/ITSV 412/Project #3- Using Python/')

from collections import Counter

# Read file directly into a Counter
with open('3.1 Four dimensions of service management.txt') as f:
    cnts = Counter(l.strip() for l in f)

# Display most common lines
cnts.most_common(1)


# Display least common lines
cnts.most_common()[-1:]


# print the answers forom the file
print(" the least requested list is:", cnts.most_common(1))
print(" the most requested list it:", cnts.most_common()[-1:])
