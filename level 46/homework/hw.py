def high_and_low(numbers):
    nums= [int(num)for num in number.split()]
    return f'{max(nums)} {min(nums)}' 


def validate_pin(pin):
    return (len(pin)==4 or len(pin)== 6) and pin.isdigit()


def greet(name): 
    return f"Hello {name.capitalize()}!"