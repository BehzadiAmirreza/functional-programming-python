# check_palindromes.py

def is_palindrome(word):
    """
    Check if a word is a palindrome.
    
    Args:
        word (str): The word to check.
    
    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    return word == word[::-1]

def all_palindromes(words):
    """
    Check if all words in a list are palindromes.
    
    Args:
        words (list): A list of words to check.
    
    Returns:
        bool: True if all words are palindromes, False otherwise.
    """
    return all(map(is_palindrome, words))

# Example usage
if __name__ == "__main__":
    # Example list of words
    words = ["radar", "level", "deified"]
    
    # Check if all words are palindromes
    result = all_palindromes(words)
    
    # Print the result
    print(result)  # Output: True