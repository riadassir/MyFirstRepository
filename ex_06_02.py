#############################################################
# Riad Assir - Coursera Python Data Strucutres Class - ex_06_02.py
# Dealing with Files
#############################################################

#FileHandle = open('mbox-short.txt')

FileName = input('Enter the file name: ')
try:
    FileHandle = open(FileName)
except:
    print('File cannot be opened: ', FileName)
    quit()

for line in FileHandle:
    print((line.rstrip()).upper())


#content = FileHandle.read()
#UpperCaseContent = content.upper()
#print (UpperCaseContent)


#################################### testing code for previous work
#count = 0
#for line in FileHandle:
#    line.rstrip()
#    if line.startswith('Subject:'):
#        count = count + 1
#    if not line.startswith('From:'):        #If you don't see the word From in the line, skip it..
#        continue
#    print(line)
#    
#print('There were', count, 'subject lines in', FileName)
######################################

