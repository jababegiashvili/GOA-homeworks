def is_isogram(string):
    string = string.Lower()
    counter = 0
    for letter in string:
        occurences = string.count(letter)
        counter += occurences
    return counter == len(string)