import sys


def RotatedArray(arr, n):
    low = 0
    high = n-1
    ans = sys.maxsize
    index = -1

    while(low <= high):
        mid = (low+high) // 2

        if(arr[low] <= arr[high]):
            if(arr[low] < ans):
                ans = low
                index = arr[low]
            break

        if(arr[low] <= arr[mid]):
            if(arr[low] < ans):
                ans = low
                index = arr[low]
            low = mid+1
        else:
            if(arr[mid] <= ans):
                ans = mid
                index = arr[mid]
            high = mid-1
    return index


arr = [4, 5, 6, 7, 0, 1, 2, 3]
n = 8
ans = RotatedArray(arr, n)
print("The Array Rotated", ans, "times")
