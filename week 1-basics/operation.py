n = int(input())
nums = list(map(int, input().split()))


def check_numbers(nums):
    for i in nums:
        if i%2!=0:
            return False
    return True

steps=0
while(1):
    if check_numbers(nums) is True:
        for i,value in enumerate(nums):
            nums[i]=value//2
            
        steps+=1
    else:
        break
print(steps)



