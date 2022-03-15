########################################################
# Riad Assir - Coursera Python Data Structures - ex_11_02.py
# Homework assignment for chapter 11
# PRETTY POWERFUL STUFF...
########################################################

# Make sure you import the library that does the regular expression stuff
import re


name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1321314.txt"
fhandle = open(name)

TotalSum = 0.0

for line in fhandle:
    # Search for any number in any given line in the file
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    if (len(x) > 0):
        print("Here are the numbers on this line:", x)

    
    # Now lets' try to get the numbers out of this line, to add them up
    for SubStr in x:
        num = float(SubStr)
        TotalSum = TotalSum + num
        print(num, TotalSum)
        #print(SubStr)

print("The End!")    


