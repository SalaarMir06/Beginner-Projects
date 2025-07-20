# print pattern
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5 

times = 5
for i in range(1, 6):
    print(" ".join(str(i)*times))
    times -= 1


