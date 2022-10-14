Linear Search:

def linear(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = ['a','b','c','d','e']
x='d'
print("element found at "+str(linear(arr, x)))

Binary Search:

def binary(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary(arr, low, mid-1, x)
        elif arr[mid] < x:
            return binary(arr, mid+1, high, x)
    else:
        return -1
arr = [21,43,5,76,34,12,2,47]
x = 76

ans = binary(arr, 0, len(arr)-1, x)

if ans != -1:
    print("element is at ", str(ans))
else:
    print("element not found")
