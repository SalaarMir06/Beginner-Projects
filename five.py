listOne = [1,2,3,1]
listTwo = [2,3,4,9]
listName = input("Enter the list name: ")
chosenList = globals().get(listName)

if chosenList[0]==chosenList[-1]:
    print(True)
else:
    print(False)
