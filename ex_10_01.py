########################################################
# Riad Assir - Coursera Python Data Structures - ex_10_01.py
# PRACTICE code
########################################################

# practice code for now

fhand = open('romeo.txt')
counts = dict()

#### for each line in the file you're reading
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    ## Now create the list of tuples
    lst = list()
    for key, val in counts.items():
        newtup = (val, key)         # Create a new tuple that's the reverse and append it to the list
        lst.append(newtup)

    lst = sorted(lst, reverse=True) #Sort the new list, with reverse order on

print("here's the sorted list")
for val, key in lst[:10]:       #Get the top 10 - from the list, into the tuple
    print(key, val)

print("done")

    
