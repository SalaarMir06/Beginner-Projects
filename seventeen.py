# fabonacci sequence

limit = int(input("Enter n times sequence runs:  "))
n = 0
k = 1
for i in range(limit):
    print(n)
    sum = n + k
    n = k
    k = sum


    