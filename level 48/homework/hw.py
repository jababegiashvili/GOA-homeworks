def simple_multiplication(number) :
    return number * 8 if number % 2 == 0 else number * 9 

def invert(lst):
    return [n * -1 for n in lst] if len(lst) > 0 else []


def string_to_array(s):
    return s.split(" ")


def monkey_count(n):
    result = []; 
    for num in range(1, n + 1):
        result.append(num); 
    return result;  


def is_isogram(string):
    return len(string) == len(set(string.lower()))


