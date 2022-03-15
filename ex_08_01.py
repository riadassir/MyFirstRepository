########################################################
# Riad Assir - Coursera Python Data Structures - ex_08_01.py
#
########################################################


### Open the file
fname = input("Enter file name: ")
fh = open(fname)


### Use lst to accumulate unique words that you will spit out later
lst = list()
CleanWord = ''

## For each line read, split the words and see if they are already found, otherwise add them to the list of unique words
for line in fh:
    #print(line.rstrip())
    WordsInOneLine = line.split()
    for word in WordsInOneLine:
        #print (word)
        #If the word we just picked is not already found, then add it to the list of unique words
        # Add logic here to find that word first
        CleanWord = word.strip()
        if CleanWord in lst:
            #print("already found", CleanWord, "-found")
            continue
        else:
            #print("new word ", CleanWord, "-new")
            lst.append(CleanWord)
            

lst.sort()
print(lst)


