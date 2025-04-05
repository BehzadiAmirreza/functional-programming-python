def binary_search(arr, key):
    def recursive_search(low, high):
        if low > high:
            return -1
        
        mid = low + (high - low) // 2  # Prevents potential overflow
        
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return recursive_search(low, mid - 1)
        else:
            return recursive_search(mid + 1, high)
    
    return recursive_search(0, len(arr) - 1)

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(arr, 5))  # Should return 4
