# 1. find max & min
 
nums = [3,7,2,9,1]
max_num=nums[0]
min_num=nums[0]
for x in nums:
    if x > max_num:
        max_num=x 
    if x < min_num:
        min_num=x 
print(max_num)
print(min_num)

# 2. remove duplicates 

cums=[1,2,2,3,4,4]
print(list(set(cums)))

# 3. frequency count

s="hello"
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
print(d)

# 4. second largest element 

dums = [10,20,4,45,99]
dums=(list(set(dums)))
dums.sort()
print(dums[-2])

# 5. sum of list

lums = [1,2,3,4]
t=0
for x in lums:
    t+=x
print(t)

# 6. count even numbers 

dums = [1,2,3,4,5,6]
count=0
for x in dums:
    if x %2==0:
        count+=1
print(count)

# 7. find maximum 

sums=[10,5,20,8]
max_num=sums[0]
for x in sums:
    if x>max_num:
        max_num=x
print(max_num)

# 8. reverse list

aums=[1,2,3,4]
print(aums[::-1])

# 9. find duplicate element 

rums=[1,2,3,3,3,4,2]
seen = set()

for x in rums:
    if x in seen:
        print(x)
        break
    seen.add(x)






