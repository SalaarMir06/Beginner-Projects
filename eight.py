# print the pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

start = int(input("Enter the beginning point: "))
stop = int(input("Enter the ending point: "))
for i in range(start,stop):
    print(str(i)*i)


