# 1. take two inputs and print thier sum 
a=10
b=3
print(a+b)

# 2. take radius as input and print area 
r=int(input("enter radius : "))
area = 3.14*r*r  
print(area)

# 3. swap two numbers --> input : c=5, d=10 output : c=10, d=5
c = 5
d = 10
c,d=d,c 
print(c,d)

# 4. convert temperature 
C  = 34
F=(C * 9/5)+32
print(F)

# 5. take a number and print its square and cube 
e = int(input("enter number : "))
square = e ** 2
cube = e ** 3
print("square",square)
print("cube",cube)

# 6. simple interest take input and print SI 
P = int(input("enter principle : "))
R = int(input("enter rate : "))
T = int(input("enter time : "))
SI = (P*R*T)/100
print("Simple Interest",SI)

# 7. take 3 numbers and print average 
x=25
y=25
z=50
average = (x+y+z)/3
print(average) 

# 8. convert minute -> hours 
m = int(input("enter minutes : "))
hours = m//60
remaining = m%60
print(hours,"hours",remaining,"minutes") 

# 9. last digit of number
n=int(input("enter a number : "))
p=n%10
print(p) 

# 10. sum of digits --> input : 123 output : 6
q=123
r=q//100
s=q//10%10
t=q%10
result = r+s+t 
print(result) 

# 11. reverse 2- digit number 
u=int(input("enter number : "))
v=u%10
w=u//10
result=(v*10)+w
print(result)  

# 12. take 5 subject marks --> print total & precentage 
total_marks=500
a=int(input("english marks : "))
b=int(input("hindi marks : "))
c=int(input("marathi marks : "))
d=int(input("science marks : "))
e=int(input("math marks : "))
total_marks_obtained = (a+b+c+d+e)
percentag = total_marks_obtained/total_marks*100
print(total_marks,percentag)      

# 13. convert days --> years,weeks,days
enter_days = int(input("days : "))
year = enter_days//365
remaining_days = enter_days-365
weeks = remaining_days//7
days = remaining_days % 7
print(year,weeks,days)





