########################################################
# Riad Assir - Coursera Python Data Structures - ex_10_02.py
# 
########################################################

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fhandle = open(name)



### Let's find the line that starts with "From " and then pick out the time (it's the 6th element in the   From line, with space separators)
HoursCounter = dict()

for line in fhandle:
    if line.startswith('From '):
        words = line.split()

        TimeString = words[5]  ### IS this the time string??
        #print (TimeString)
        # Now let's pick the first part of the time (the hour)
        TimeStampPieces = TimeString.split(':')
        HourStr = TimeStampPieces[0]

        HoursCounter[HourStr] = HoursCounter.get(HourStr, 0) + 1

#####################################
#Now we have the HoursCounter with all the hours.  We need to sort them by hour

    ## Now create the list of tuples
    lst = list()
    for key, val in HoursCounter.items():
        newtup =  (key, val)         # Create a new tuple that's the reverse and append it to the list
        lst.append(newtup)

    lst = sorted(lst) #, reverse=True) #Sort the new list, with reverse order on

#print("here's the sorted list")
for val, key in lst:      
    print(val, key)

