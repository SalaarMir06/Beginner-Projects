# write a python code to create new list containing
# odd numbers from first and even numbers from second list 

listOne = []
listTwo = []

n = int(input("Enter the length of list: "))

for i in range(n):
    number = int(input("Enter a list of numbers: "))
    listOne.append(number)

for i in range(n):
    secNum = int(input("Enter a second list of numbers: "))
    listTwo.append(secNum)


oddNum = []

for i in listOne:
    if i%2 != 0:
        oddNum.append(i)
   

evenNum = []

for i in listTwo:
    if i%2 == 0:
        evenNum.append(i)
    

finalList = oddNum + evenNum
print(f"finaList {finalList}")