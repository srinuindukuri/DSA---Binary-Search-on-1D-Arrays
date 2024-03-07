def search(arr, target):
    n = len(arr)
    low = 0
    high = n-1
    while(low <= high):
        mid = (low+high) // 2

        if (arr[mid] == target):
            return True

        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue

        if (arr[low] <= arr[mid]):
            if (arr[low] <= target and target <= arr[mid]):
                high = mid-1
            else:
                low = mid+1

        else:
            if (arr[mid] <= target and target <= arr[high]):
                low = mid+1
            else:
                high = mid-1
    return False


arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
target = 3
ans = search(arr, target)
if not ans:
    print("Target not found...")
else:
    print("The target is present... ")
