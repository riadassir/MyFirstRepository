########################################################
# Riad Assir - Coursera Python Data Structures - ex_06_03.py
#
########################################################



# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0
Total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    ## Assuming the number starts with a 0, and goes to the end of the string
    num =line[line.find('0'):]
    Fnum = float(num)
    Total = Total + Fnum  #THis is the total of all the numbers at the end of each of these lines found
    count = count + 1

    #print(count, line, Total)
    

Average = Total / count
print('Average spam confidence:', Average)
