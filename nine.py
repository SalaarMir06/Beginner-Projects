# write a programme to check whether a number is palindrome or not

number = str(input("Enter a number: "))

if number[::-1] == number:
    print(f"Original number : {number}")
    print(f"Yes, given number is palindrome number")
else:
    print(f"Original number : {number}")
    print(f"Oops! given number isn't palindrome number")
