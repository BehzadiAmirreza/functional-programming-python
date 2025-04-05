def calculate_average(*args, round_to=None):
    # Calculate the count of numbers
    count = len(args)
    
    # Calculate the arithmetic mean
    if count == 0:
        average = 0  # Handle case with no arguments
    else:
        average = round(sum(args) / count)
    
    # Round the average if round_to is specified
    if round_to is not None:
        average = round(sum(args) / count, round_to)
    
    # Print the count and average as shown in the target usage
    print(f"Count: {count}, Average: {average}")
    
    # Return the average
    return average


# Example usage
if __name__ == "__main__":
    # Test case 1: No rounding
    result1 = calculate_average(1, 2, 3, 4, 5)
    print(result1)  # Expected output: 3.0
    
    # Test case 2: Rounding to 4 decimal places
    result2 = calculate_average(10, 20, 30, 41, 50.12312, round_to=4)
    print(result2)  # Expected output: 30.2246
    
    # Test case 3: Empty input
    result3 = calculate_average()
    print(result3)  # Expected output: 0