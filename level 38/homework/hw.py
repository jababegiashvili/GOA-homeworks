def boolean_to_string(b):
     return str(b)
 


def basic_op(operator, value1, value2):
    if operator == '+': return value1 + value2
    if operator == '-': return value1 - value2
    if operator == '*': return value1 * value2
    if operator == '/': return value1 / value2



def maps(a):
    new=[]
    for e in a:
        new.append(e*2)
    return new
