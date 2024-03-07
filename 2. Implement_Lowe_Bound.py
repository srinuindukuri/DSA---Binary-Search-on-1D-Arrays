# What is Lower Bound?
# The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is
#  greater than or equal to a given key i.e. x.

# The lower bound is the smallest index, ind, where arr[ind] >= x. But if any such index is not found, the lower bound
#  algorithm returns n i.e. size of the given array.

# ------------------------------------------------------------------------------------------------------------------------

def LowerBound(arr, x, n):
    low = 0
    high = n-1
    ans = n

    while(low <= high):
        mid = (low+high) // 2

        if arr[mid] >= x:
            ans = mid

            high = mid-1
        else:
            low = mid+1
    return ans


if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    x = 8
    n = 5
    ind = LowerBound(arr, x, n)
    print("The Lower bound is..", ind)
