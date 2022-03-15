########################################################
# Riad Assir - Coursera Python Data Structures - ex_09_01.py
#
########################################################

# practice code for now

counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

print("*** Now, we'll go through it in a for loop***")
for key in counts:
    print(key, counts[key])      


print ('Done!')
