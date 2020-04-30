import math

nums = [1,2,7,6,4]
numslen = len(nums)
answer = 0
plus = 0
for i in range(len(nums)):
    sec = i+1
    while numslen>=sec:
        thr = sec+1
        while numslen>thr:
            plus = nums[i]+nums[sec]+nums[thr]
            check = 2
            out = 0
            while math.sqrt(plus) >= check:
                if plus%check==0:
                    out+=1
                check+=1
            if out==0:
                answer+=1
            thr+=1
        sec += 1

print(answer)
