def firstOccurence(arr, n, k):
    low = 0
    high = n-1
    first = -1

    while(low <= high):
        mid = (low+high) // 2
        if(arr[mid] == k):
            first = mid
            high = mid-1
        elif(arr[mid] < k):
            low = mid+1
        else:
            high = mid-1
    return first


def lastOccurence(arr, n, k):
    low = 0
    high = n-1
    last = -1

    while(low <= high):
        mid = (low+high) // 2
        if(arr[mid] == k):
            last = mid
            low = mid+1
        elif(arr[mid] < k):
            low = mid+1
        else:
            high = mid-1
    return last


def firstAndLastPosition(arr, n, k):
    first = firstOccurence(arr, n, k)
    if first == -1:
        return (-1, -1)
    last = lastOccurence(arr, n, k)
    return (first, last)


arr = [2, 4, 6, 8, 8, 8, 11, 13]
n = 8
k = 8
ans = firstAndLastPosition(arr, n, k)
print("The first and last occurence are..", ans[0], ans[1])
