# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# Iterative Implementation
# Solution:

def BinarySearch(arr, target):
    n = len(arr)
    low = 0
    high = n-1

    while(low <= high):
        mid = low + high // 2

        if (arr[mid] == target):
            return mid
        elif target > arr[mid]:
            low = mid+1
        else:
            high = mid-1
    return -1


if __name__ == "__main__":
    arr = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 6
    ind = BinarySearch(arr, target)
    if ind == -1:
        print("The target is not present.")
    else:
        print("The target is at index:", ind)

# ------------------------------------------------------------------------------------------------------------------------

# Recursive Implementation


def BinarySearch(arr, low, high, target):
    if low > high:
        return -1   # Base Case

    # Perform the steps
    mid = (low+high) // 2
    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return BinarySearch(arr, mid+1, high, target)
    return BinarySearch(arr, low, mid-1, target)


def search(arr, target):
    return BinarySearch(arr, 0, len(arr)-1, target)


arr = [3, 4, 6, 7, 9, 12, 16, 17]
target = 6
ind = search(arr, target)
if ind == -1:
    print("Target not present..")
else:
    print("The target value is..", ind)

# Time Complexity -> O(logN)
