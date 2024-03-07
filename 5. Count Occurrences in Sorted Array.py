# Problem Statement: You have been given a sorted array/list of integers 'arr' of size 'n' and an integer 'x'.
# Find the total number of occurrences of 'x' in the array/list.

# Example:
# Input: 'n' = 7, 'k' = 3
# 'arr' = [1, 1, 1, 2, 2, 3, 3]
# Output: 2

# Explanation: Total occurrences of '3' in the array 'arr' is 2.
# -----------------------------------------------------------------------------------------------------------------------

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


def count(arr, n, k):
    first, last = firstAndLastPosition(arr, n, k)
    if first == -1:
        return 0
    return last - first + 1


arr = [1, 1, 1, 2, 2, 3, 3]
n = 7
k = 3
ans = count(arr, n, k)
print("The number of occurrences is:", ans)
