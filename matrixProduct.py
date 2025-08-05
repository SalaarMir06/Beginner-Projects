import numpy as np 

N = int(input())

A = []
for i in range(N):
  A.append(list(map(int, input().split())))

B = []
for i in range(N):
  B.append(list(map(int, input().split())))

product = np.dot(A, B)

print(product)
