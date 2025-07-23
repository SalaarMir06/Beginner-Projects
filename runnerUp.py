if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

highest = max(arr)
sorting = [i for i in arr if i != highest]

if sorting:
    runnerUp = max(sorting)
    print(runnerUp)
