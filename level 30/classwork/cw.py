def min_and_max_num(num):
    num=list(int, num.split())
    highest=max(num)
    lowest=min(num)
    return f"{highest}{lowest}"
print(min_and_max_num(" 2 4 6 8 "))