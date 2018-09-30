#COMPLETED

data = [5, 2, 1, 3, 3, 2]

def getResult(data):
    nums = [True]
    for i in range(0, len(data)):
        if data[i] < 0:
            continue        
        if len(nums) <= data[i]:
            nums = nums + [False]*(data[i]-len(nums)+3)        
        nums[data[i]] = True
        
    for i in range(0, len(nums)):
        if nums[i] == False:
            return i
            break

print(getResult(data))    