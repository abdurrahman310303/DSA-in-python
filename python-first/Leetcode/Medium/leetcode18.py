def SUM(nums,target):
    result = []
    nums.sort()

    for i in range(0,len(nums)):
        
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                for l in range(k+1,len(nums)):
                    sumx = nums[i] + nums[j] + nums[k] + nums[l]
                    if sumx == target:

                        result.append([nums[i], nums[j], nums[k], nums[l]])
        
    unique_result = [list(tup) for tup in set(tuple(lst) for lst in result)]
    
    return unique_result


inputNums = [-5,5,4,-3,0,0,4,-2]


target = 4
res = SUM(inputNums,target)

print(f"The result is {res}")

