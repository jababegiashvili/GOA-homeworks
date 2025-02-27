def math_position(x, position):
    
    arr = []
    while x > 0:
        sum = x % position
        arr.append(sum)
        x = x // position
    return arr[::-1]
print(math_position(5, 8))
 
