########################################################
# Riad Assir - Coursera Python Data Structures - ex_09_02.py
# PRACTICE code
########################################################

# practice code for now

fname = input('Enter file name:')
fhandle = open (fname)

### Declare that counts is a dictionary
counts = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

BiggestCount = None
BiggestWord = None
for word,count in counts.items():
    if BiggestCount is None or count > BiggestCount:
        BiggestWord = word
        BiggestCount = count
    print(word, count, BiggestWord, BiggestCount)


print ("End!")
