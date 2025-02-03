def removeNegative(arr):
    newArr = []
    for i in arr:
        if i >= 0:
            newArr.append(i)
    
    for i in newArr:
        print(i, end=' ')

arr = [1, -3, 2, 6, -7]
removeNegative(arr)






