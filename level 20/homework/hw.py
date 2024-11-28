arr=("a , e ,d ,g ,u ,l ,c ,q , i ,d ,i ")
counter= 0
is_count=("a, e, i ,o ,u")

for char in arr:
    if char == is_count:
        counter + 1
print(counter)
