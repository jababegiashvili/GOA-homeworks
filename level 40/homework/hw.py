def stray(arr):
    for integer in arr:
        if arr.count(integer) == 1:
            return integer
        

def solution(nums):
    if type (nums) == list:
        return sorted(nums)
    else:
        return []
    

    def capitals(word):
     result= []
    for index in range(len(word)):
        if word[index].isupper():
            result.append(index)
    return result