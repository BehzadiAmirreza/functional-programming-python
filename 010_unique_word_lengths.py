import string

sentence = "Hello, World! This is a test. Isn't it great to explore Python's capabilities? Yes, indeed!"

translator = str.maketrans('', '', string.punctuation)
cleaned_sentence = sentence.translate(translator)

unique_lengths = {len(word) for word in cleaned_sentence.split()}
print(unique_lengths)