# Binary Search
# Take a sorted list and an element to find, return the index of the element if found or return null if not found
# Search the list by testing the middle item
    # if mid is lower than the element -> new boundary is low to mid - 1
    # if mid is higher than the element -> new boundary is mid + 1 to top
# if the entire list is searched and item is not found, return null

# define the method signature
def binary_search(elements, item):
    low = 0
    high = len(elements) - 1

    while low <= high:
        search_index = (low + high) // 2
        guess = elements[search_index]
        
        if guess == item:
            return search_index
        elif guess < item:
            low = search_index + 1
        elif guess > item:
            high = search_index - 1
    
    return None

def main():
    elements = [1, 5, 10, 12, 15, 35, 40, 45, 49, 50]
    item = 50
    
    print("The result is:", binary_search(elements, item))
    
if __name__ == "__main__":
    main()
    