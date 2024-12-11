nums = [3,2,1,2,1,7]

nums.sort()
step = 0
i = 0
l = len(nums)
while(i < l):
    n = nums.count(nums[i])
    if n>1:
        j = i + 1
        for k in range(n-1):
            nums[j]+=1
            j+=1
    step+=n-1
    i+=1
    
print(step)
        