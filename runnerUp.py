if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

highest = arr[0]

for i in arr:
    if i > highest:
        highest = i

runnerUp = arr[0]

for i in arr:
    if i != highest and i > runnerUp:
        runnerUp = i

print(runnerUp)
