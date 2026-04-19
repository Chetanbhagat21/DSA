# 6. frequency of elements 

nums=[1,2,2,3,3,3]
dic={}
for num in nums:
    if num in dic:
        dic[num]+=1
    else:
        dic[num]=1
print(dic)

# 7. check if list is sorted 

lums = [1,2,3,4]
is_sorted = True
for i in range(len(nums)-1):
    if nums[i]>nums[i+1]:
        is_sorted=False
        break 
print(is_sorted)

# 8. merge two list 

a = [1,2,3]
b = [4,5,6]
for num in b:
    a.append(num)
print(a)
        
# 9. second smallest element

nums=[10,20,4,45,99]

smallest = float('inf')
second_smallest = float('inf')

for num in nums:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num > smallest and num < second_smallest:
        second_smallest = num

print(second_smallest)

# 10. find missing number 

nums = [1,2,4,5]

n = len(nums) + 1   # because one number is missing

expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

missing = expected_sum - actual_sum

print(missing)








