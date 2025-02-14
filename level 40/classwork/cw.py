def friend(x):
    return [name for name in x if len(name) == 4]


from typing import Callable

def add(n: int) -> Callable:
    return lambda x: x + n



def row_sum_odd_numbers(n):
    sum_of_odd_integers = []
    for layer in range(1,n+1):
        sum_of_odd_integers.append(layer + layer**2)
    return max(sum_of_odd_integers)