# 1. if,else,elif

num = -1
if num>0:
    print("positive")
else:
    print("negative")
    

# 2. multiple conditions 

num=0
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")
    
# 3. nested if 

num = 10
if num>0:
    if num %2==0:
        print("positive even")