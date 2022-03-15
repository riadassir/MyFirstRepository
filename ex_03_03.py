################# Assignment - Python class for beginners

score = input("Enter Score: ")
fScore = float(score)
if ((fScore < 0.0) or (fScore >1.0)):
    print("Out of Range")
else:
    if (fScore < 0.6):
        print('F')
    elif ((fScore >= 0.6) and (fScore < 0.7)):
        print('D')
    elif ((fScore >= 0.7) and (fScore < 0.8)):
        print ('C')
    elif ((fScore >= 0.8) and (fScore < 0.9)):
        print ('B')
    elif ((fScore > 0.9) and (fScore < 1.0)):
        print ('A')
    else:
        print ('Out of Range')
