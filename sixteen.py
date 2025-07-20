# write a program to check palindrome number

number = input("Enter a number : ")
palindrome = number[::-1]

if number == palindrome:
    print(f"{number} is a palindrome number")
else:
    print(f"{number} isn't a palindrome")


