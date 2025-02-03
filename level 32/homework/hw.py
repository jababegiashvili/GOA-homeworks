def string_to_array(s):
    if s== ' ':
        return s.split()
    


def string_to_number(s):
    return int(s)


def fake_bin(number_string):
    binary_string =''
    for number in number_string:
        if int(number) < 5:
            binary_string += '0'
        else:
            binary_string += '1'
            
        return binary_string
    
    
