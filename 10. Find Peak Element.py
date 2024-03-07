def FindPeakElement(arr):
    n = len(arr)   # Length of array:

    # Edge Cases:
    if(n == 1):
        return 0
    if (arr[0] > arr[1]):
        return 0
    if (arr[n-1] > arr[n-2]):
        return n-1

    low = 1
    high = n-2

    while(low <= high):
        # If arr[mid] is the peak:
        mid = (low + high) // 2
        if(arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]):
            return mid

        # If we are in the left:
        if (arr[mid] > arr[mid-1]):
            low = mid + 1

        # If we are in the right:
        # Or, arr[mid] is a common point:
        else:
            high = mid-1

    # Dummy return Statement:
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
ans = FindPeakElement(arr)
print("The Peak Element is at index at..", ans)
