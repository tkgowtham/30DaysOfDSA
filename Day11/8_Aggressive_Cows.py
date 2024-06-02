def canWePlace(arr, dist, cows):
    countCows = 1
    last = arr[0]
    for i in range(1, len(arr)):
        if arr[i] - last >= dist:
            countCows += 1
            last = arr[i]
        if countCows >= cows:
            return True

    return False

t = int(input())
n, cows = map(int, input().split(' '))
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
n = len(arr)
low = 0
high = n - 1
while low <= high:
    mid = (low + high) // 2
    if canWePlace(arr, mid, cows):
        low = mid + 1
    else:
        high = mid - 1


print(high)
