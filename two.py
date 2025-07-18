# write a program to iterate through the first 10 numbers
# and in each iteration print the sum of the current and prevous number
print("Printing current and previous number sum in a range(10)")

prevNum = 0
for number in range(10):
    sum = prevNum + number
    print(f"Current Number {number} Previous Number {prevNum} Sum : {sum}")
    prevNum = number
 