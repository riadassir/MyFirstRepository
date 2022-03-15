
########################################################
# Riad Assir - Coursera Python Data Structures - ex_08_02.py
#
# You will parse the From line using split() and print out the second word
# in the line (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
########################################################



fname = input("Enter file name: ")

if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)

count = 0

## For each line read, see if it starts with a "From" and then split the words 
for line in fh:
    #print(line.rstrip())
    if line.startswith('From '):
        WordsInOneLine = line.split()
        email = WordsInOneLine[1]   # Typically comes after the From part
        print(email)
        count = count +1
        
            
print("There were", count, "lines in the file with From as the first word")

 
