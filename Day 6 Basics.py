# functions 

def greet():
    print("hello")
greet()

# functions with parameters

def add(a,b):
    return a+b 
print(add(2,3))

# recursion 
''' 
Every recursive function must have:
Base Case → stops recursion
Recursive Case → function calls itself
'''
def print_numbers(n):
    if n == 0:   # Base case
        return
    print(n)
    print_numbers(n - 1)  # Recursive call

print_numbers(5)