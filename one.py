# write a program to return product only if the product is equal to or less than 1000
# otherwise print sum of numbers


firstVar = int(input("Enter a number "))
secondVar = int(input("Enter a number "))
prodVar = firstVar*secondVar

if prodVar <= 1000:
    print("product is equal to ", firstVar*secondVar)
else: 
    print("sum is equal to ", firstVar+secondVar)
