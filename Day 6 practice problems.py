# 1. function for even/odd

def check_even(n):
    if n % 2==0:
        return "True"
    else:
        return "False"
print(check_even(11))

# 2. function for max of 3 

def function_max(a,b,c):
    if a>= b and a>= c:
        return a 
    elif b>=a and b>=c:
        return b 
    else:
        return c 
print(function_max(12,15,25))
    
# 3. function for factorial 

def function_factorial(n):
    if (n==0 or n==1):
         return 1
    return n * function_factorial(n-1)

print(function_factorial(10))









