# write a program to display numbers divisible by 5
list = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    elements = int(input("Number : "))
    list.append(elements)

print(f"Give list is {list}")
print("Divisble by 5 are: ")
length = len(list)

for i in range(length):
    if list[i]%5 == 0:
        print(list[i])
    else:
        None

