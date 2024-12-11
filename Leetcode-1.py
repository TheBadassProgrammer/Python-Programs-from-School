nums = [3,2,4]
target = 6
i = 0
j = 1
while i < len(nums):
    if (target == nums[i] + nums[j]) and (i!=j):
        array = [i,j]
        break
    else:
        if j < len(nums)-1:
            j += 1
        else:
            i += 1
            j = 0

print (array)