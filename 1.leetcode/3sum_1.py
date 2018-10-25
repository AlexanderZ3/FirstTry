'''
solu = []
nums = [-1,0,1,2,-1,-4]
length = len(nums)
for i in range(length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            if nums[i]+nums[j]+nums[k] == 0:
                solu.append([nums[i],nums[j],nums[k]])
for i in range(len(solu)):
    if i+1 < len(solu):
        for j in range(i+1,len(solu)):
            solu[i].sort()
            solu[j].sort()
            if (solu[i][0] == solu[j][0]) and (solu[i][1] == solu[j][1]) and (solu[i][2] == solu[j][2]):
                del solu[j]
print(solu)
'''

# Another method, saving time

solu = []
nums = [-1,0,1,2,-1,-4]
nums.sort()
lens = len(nums)
i = 0
while (i< lens-2):
    if(nums[i]!=nums[i-1] or i==0):
        target = 0-nums[i]
        left = i+1
        right = lens-1
        while(left != right):
            if(nums[left]+nums[right]== target):
                solu.append([nums[i],nums[left],nums[right]])
                while(left<right):
                    left+=1
                    if (nums[left] != nums[left-1]):
                        break
                while(right>left):
                    right-=1
                    if(nums[right] != nums[right+1]):
                        break
            elif(nums[left]+nums[right] > target):
                right-=1
            elif(nums[left]+nums[right] < target):
                left+=1
    i+=1
print(solu)
