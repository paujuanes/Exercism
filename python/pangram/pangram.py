def is_pangram(sentence):
    import string
    alphabet = list(string.ascii_lowercase)  # Creating an ASCII alphabet
    # Removing any punctuation and lowercasing
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    sentence = sentence.lower()
    # Creating a dictionary using the alphabet and checking all sentence's letters
    pangram = {k:(True if k in sentence else False) for k in alphabet}
    return all(pangram.values())  # Checking the dictionary values