def bool_to_word(boolean):
    return "Yes" if boolean else "No"


def remove_char(s):
    return s[1:-1]
    

def string_to_number(s):
    return int(s)



def no_space(x):

    result = x.replace(" ", "")
    return result


def sum_array(a):
    return sum(a) if a else 0