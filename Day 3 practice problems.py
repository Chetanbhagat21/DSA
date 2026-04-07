# 1. print 1 to N 

i=1
n=int(input("enter number : "))
while i <= n:
    print(i)
    i+=1

# 2. factorial

num = 5
factorial = 1
for i in range(1,num+1):
    factorial *=i
print(f"the factorial {num} is {factorial} ")

# 3. fibonacci series

n=5
a=0
b=1
for i in range(n):
    print(a)
    next=a+b 
    a=b 
    b=next 
 
# 4. star pattern 

for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

# 5. reverse pattern

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()
    
# 6. pyramid pattern 

n=5
for i in range(n+1):
    for j in range(n-i):
            print(" ",end="")
    for j in range(2*i-1):
            print("*",end="")
    print()
        
    
    
