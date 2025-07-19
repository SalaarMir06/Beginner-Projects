# write a program to find how often a word has occured in a string 

string = input("Enter a string : ")
word = input("Enter the word : ")

occurences = string.count(word)

print(f"{word} appeared {occurences} times")

