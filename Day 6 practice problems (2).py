# 4. fibonacci using recursion 

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))

# 5. sum of digits 
# using recursion
def sum_digits(n):
    if n==0:
        return 0
    return (n%10) + sum_digits(n//10)
print(sum_digits(123))

# using loop 
def sum_of_digits(n):
    total = 0
    
    while n > 0:
        digit = n % 10      
        total += digit      
        n = n // 10         
    
    return total

print(sum_of_digits(123))  

# 6. reverse string 

def reverse_string(s):
    if len(s) <= 1:   
        return s
    
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello")) 









