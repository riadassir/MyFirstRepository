######################################### Python Ex_05_03
# last homework for the beginner's class
#########################################


largest = 0.0
smallest = 0.0
FirstTimeWeRunThisProgram = True

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            fNum = float (num)
        except:
            print ("Invalid input")
            continue;

        if FirstTimeWeRunThisProgram:
            largest = fNum
            smallest = fNum
            FirstTimeWeRunThisProgram = False
            
        if fNum > largest:
            largest = fNum
        elif fNum < smallest:
            smallest = fNum
            
        

print("Maximum", largest)
print ("Minimim", smallest)

