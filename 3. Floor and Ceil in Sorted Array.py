def GetFloor(arr, x, n):
    low = 0
    high = n-1
    ans = -1

    while(low <= high):
        mid = (low + high) // 2

        if(arr[mid] <= x):
            ans = arr[mid]
            low = mid + 1
        else:
            high = mid-1
    return ans


def GetCeil(arr, x, n):
    low = 0
    high = n-1
    ans = -1

    while(low <= high):
        mid = (low + high) // 2

        if(arr[mid] >= x):
            ans = arr[mid]
            high = mid - 1
        else:
            low = mid+1
    return ans


def GetFloorCeil(arr, x, n):
    f = GetFloor(arr, x, n)
    c = GetCeil(arr, x, n)
    return(f, c)


arr = [3, 4, 4, 7, 8, 10]
n = 6
x = 5
ans = GetFloorCeil(arr, x, n)
print("The Floor and Ceil are..", ans[0], ans[1])
