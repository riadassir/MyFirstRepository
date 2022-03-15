#######################################################
# Riad Assir - Coursera Python Data Structures - ex_09_03.py
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
EmailCounter = dict()    #We will store the {key, value} pairs in EmailCounts

## For each line read, see if it starts with a "From" and then split the words 
for line in fh:
    if line.startswith('From '):
        WordsInOneLine = line.split()
        email = WordsInOneLine[1]   # Typically comes after the From part
        count = count +1
        EmailCounter[email] = EmailCounter.get(email, 0) + 1
        #print(email, EmailCounter[email])



###################### Now let's find the highest count
BiggestCount = None
BiggestWord = None
for word,count in EmailCounter.items():
    if BiggestCount is None or count > BiggestCount:
        BiggestWord = word
        BiggestCount = count
    #print(word, count, BiggestWord, BiggestCount)

#print("..and the winner is....")
print (BiggestWord, BiggestCount) 

