from functools import reduce

def run_length_encode(s):
    def reducer(acc, char):
        # If the accumulator is not empty and the current character matches the last character in the accumulator
        if acc and char == acc[-1][0]:
            # Increment the count of the last character
            acc[-1] = (char, acc[-1][1] + 1)
        else:
            # Append a new tuple (char, 1) to the accumulator
            acc.append((char, 1))
        
        return acc
    
    # Use reduce to build the list of (char, count) tuples
    encoded_pairs = reduce(reducer, s, [])  # Example: [("A", 2), ("B", 1), ("C", 2), ...]
    
    # Convert the list of tuples into the encoded string
    encoded_str = "".join(f"{char}{count}" for char, count in encoded_pairs)
    
    return encoded_str

# Example usage:
print(run_length_encode("AABCCDEEEE"))  # Output: "A2B1C2D1E4"