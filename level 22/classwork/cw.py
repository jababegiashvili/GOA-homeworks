arr = list(range(1000))
 
list_of_odd =[]
list_of_even =[]
for i in range(1000) :
     if i % 2 == 0:
        list_of_even.append(i)
else:
    list_of_odd.append(i)
print(list_of_odd)
print(list_of_even)
