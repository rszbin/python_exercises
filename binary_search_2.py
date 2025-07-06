# binary_search_2

# returns the index of the target item in the array, or None
def binary_search(items, target):
    low = 0
    high = len(items) - 1
    
    while low <= high:
        midpoint = (low + high) // 2
        guess = items[midpoint]
        
        if target == guess:
            return midpoint
        elif target < guess:
            high = midpoint - 1
        elif target > guess:
            low = midpoint + 1
        
    return None

def main():
    items = [10, 20, 30, 45, 50, 66, 77, 90]
    target = 20
    
    return print(binary_search(items, target))

if __name__ == "__main__":
    main()