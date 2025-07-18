# write a program to remove characters from a 
# string from 0 to n and return a new string

string = "I wanna learn to code"
n = int(input("Enter the range to be removed ( 0 to n ): "))
word = input("Input the word to be entered: ")
remove = string[n:]
join = word + remove 
print(join)

#let's define a function for feasibility
def charRem(n, word):
    remove = string[n:]
    join = word + remove
    print(join)

