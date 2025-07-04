# Binary Search Implemented in Python

# given an array of integers sorted in ascending order, and a target integer, write a function to search target in enums. if target exists then return it's index, otherwise return -1

# 1. define a sorted array
# 2. find the middle of the array
# 3. check for a match, define the search

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        testitem = arr[mid]
        
        if testitem == x:
            return mid
        elif x < testitem:
            high = mid
        elif x > testitem:
            low = mid
        
    return -1 # if we exit the loop without finding the item, it doesnt exist
            
items = [1, 2, 5, 6, 7, 10, 22, 25, 30, 55, 56, 100]
x = 56

result = binary_search(items, x)

print(result)