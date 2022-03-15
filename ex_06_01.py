##################################################
# Riad Assir - Assignment 06_03 Python Data Structures class - Coursera


text = "X-DSPAM-Confidence:    0.8475"

## Assuming the number starts with a 0, and goes to the end of the string
num =text[text.find('0'):]
Fnum = float(num)

print(Fnum)
