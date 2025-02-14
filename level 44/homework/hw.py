def row_sum_odd_numbers(n):
    sum_of_odd_integers =[]
    for layer in range (1,n+1):
        sum_of_odd_integers.append(layer = layer**2)
    return max(sum_of_odd_integers)


def binary_array_to_number(arr):
    # binary = ""
    #for number in arr:
    # binary +=str(number)
    #print(int(binary.2))
   return int("".join([str(number)for number in arr ]),2)