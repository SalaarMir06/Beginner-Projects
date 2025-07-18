# write a program to accept a string and display characters present
# at even indexes
string = input("Enter a string : ")
print(f"Original string is {string}")
print("Printing only even index chars")
for i in string[::2]:
    print(i)
