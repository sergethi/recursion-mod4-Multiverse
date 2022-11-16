# Write a function, reverseArray, that accepts an array as an argument and returns a reversed copy of that array.
# Use recursion. Don’t mutate the original array.

def reverseArray(arr):
    arrCopy = arr.copy()

    def recursion(arr2):
        if len(arrCopy) == 1: return arrCopy
        lastVal = arrCopy.pop()
        return [lastVal] + recursion(arrCopy)
    return recursion(arrCopy)




arr = [1,2,3,4];
reversedArr = reverseArray(arr);

print(reversedArr) # [4,3,2,1]
print(arr) # [1,2,3,4]