from math import *

def merge(arr : list[int], temp_arr : list[int], low : int, mid : int, high : int) -> int:
    count = 0
    left = low
    right = mid + 1
    k = low
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp_arr[k] = arr[left]
            left += 1
        else:
            temp_arr[k] = arr[right]
            right += 1
            count += mid - left + 1  #counted here
        k += 1

    while left <= mid:
        temp_arr[k] = arr[left]
        left += 1
        k += 1

    while right <= high:
        temp_arr[k] = arr[right]
        right += 1
        k += 1

    for i in range(low, high + 1):
        arr[i] = temp_arr[i]
        
    return count

def mergeSort(arr : list[int], temp_arr: list[int], low : int, high : int) -> int:
    count = 0
    if low >= high:
        return count
    mid = floor((low + high) / 2)
    count += mergeSort(arr, temp_arr, low, mid)
    count += mergeSort(arr, temp_arr, mid + 1, high)
    count += merge(arr, temp_arr, low, mid, high)
    return count # all counts added and returned

def getInversions(arr, n) :
	# Write your code here.
    temp_arr = [0] * n
    return mergeSort(arr, temp_arr, 0,n-1)

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))
