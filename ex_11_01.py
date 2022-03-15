########################################################
# Riad Assir - Coursera Python Data Structures - ex_11_01.py
# THIS IS FOR PRACTICE PURPOSES ONLY - HAVING FUN WITH REGULAR EXPRESSIONS
# PRETTY POWERFUL STUFF...
########################################################

# Make sure you import the library that does the regular expression stuff
import re


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fhandle = open(name)


for line in fhandle:
    # Search for lines that start with 'Details: rev=' followed by numbers and '.' - print the number if >0
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)+', line)
    if (len(x) > 0):
        print("Here's the Details number:", x)
    # Now lets' try to get all the email addresses on the "From" line
    y= re.findall('^From (\S+@\S+)', line)
    if (len(y) > 0):
        print("Here's who it's from:", y)
        #Now try to get only the server name, from the email address you pulled on the FROM line
        ServerName = re.findall('@([^ ]*)', line)  # Find all the characters after the @sign, and before the space
        print("Server: ", ServerName)


print("The End!")    


