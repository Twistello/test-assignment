nums = [1,2,0,3,0]

result = []
nums.sort()
for i, a in enumerate(nums):
    j = i+1
    k = len(nums)-1
    while j < k:
        mult = a * nums[j] * nums[k]
        if mult == 0:
            result.append([a,nums[j],nums[k]])
        k -= 1

print(result)

