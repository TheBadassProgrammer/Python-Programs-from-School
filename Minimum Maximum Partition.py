# from math import ceil

# def count(st):
#     dic = {}
#     for s in st:
#         if s not in dic.keys():
#             dic[s] = 1
#         else:
#             dic[s] += 1
#     return(max(dic.values()))

# def minPartition(s,k):
#     lst = []
#     f = ceil(len(s)/k)
#     k = f

#     i = 0
#     while(True):
#         lst.append(s[i:k])
#         i = i + f
#         k = k + f
#         if k>len(s)+f:
#             break

#     if k%2==0:
#         lst.pop()

#     countLst = []
#     for word in lst:
#         x = count(word)
#         countLst.append(x)
#     print(max(countLst))
    

# minPartition("aaaabbbb",2)

    
from math import ceil
class Solution:
    def count(st):
        dic = {}
        for s in st:
            if s not in dic.keys():
                dic[s] = 1
            else:
                dic[s] += 1
        return(max(dic.values()))
    
    def minPartition(s, k):
        lst = []
        f = ceil(len(s)/k)
        k = f
        
        i = 0
        while(True):
            lst.append(s[i:k])
            i = i + f
            k = k + f
            if k>len(s)+f:
                break
    
        if k%2==0:
            lst.pop()
    
        countLst = []
        for word in lst:
            x = Solution.count(word)
            countLst.append(x)
        print(max(countLst))

Solution.minPartition("aaaabbbb", 2)