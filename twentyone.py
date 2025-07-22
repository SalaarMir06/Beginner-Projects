# write a program to check whether a user entered string 
# contains any digit using a for loop

string = input("Enter a string: ")

for i in string:
    if i >= "0" and i <="9":
        print("the string contains  digit")
        break
    else:
        None

# or 

# string = input("Enter a string: ")
# for char in string:
#     if char.isdigit():
#         print("The string contains a digit.")
#         break
# else:
#     print("The string does not contain any digits.")
