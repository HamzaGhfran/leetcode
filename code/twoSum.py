def twoSum(list,target):
    dict = {}
    for i in range(len(list)):
        dict[list[i]] = i
    for i in range(len(list)):
        res = target - list[i]
        if res in dict and dict[res] != i:
            return(dict[res],i)
    return -1
list = [2, 7, 11, 15]
target = 9
res = twoSum(list,target)
print(res)