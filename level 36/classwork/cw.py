def get_count(sentence):
    vowels ="aeiou"
    
    vowels_count = 0
    for char in sentence:
        if char.lower() in vowels:
            vowels_count += 1
    return vowels_count