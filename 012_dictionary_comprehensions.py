# Input
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
frequencies = [15, 8, 20, 5, 12, 3, 10]

# Task 1: Create a frequency dictionary
frequency_dict = {word: freq for word, freq in zip(words, frequencies)}
print("Frequency Dictionary:", frequency_dict)

# Task 2: Filter the dictionary
filtered_dict = {word: freq for word, freq in frequency_dict.items() if freq > 10}
print("Filtered Dictionary (freq > 10):", filtered_dict)

# Task 3: Transform the dictionary
transformed_dict = {freq: [word for word, f in frequency_dict.items() if f == freq] for freq in set(frequency_dict.values())}
print("Transformed Dictionary:", transformed_dict)

# Task 4: Create a word-length dictionary
word_length_dict = {word: len(word) for word, freq in frequency_dict.items() if freq > 5}
print("Word-Length Dictionary (freq > 5):", word_length_dict)