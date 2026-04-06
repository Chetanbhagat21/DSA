# 1. Even or Odd

a=int(input("enter a number : "))
if a %2==0:
    print("this is even : ",a)
else:
    print("this is odd : ",a)

# 2. Largest of 3 numbers

b=10
c=20
d=15
if b>c:
    print("this is the largest number : ",b)
if c>d:
    print("this is the largest number : ",c)
elif d>b>C:
    print("this is the largest number : ",d)

# 3. grade system 

num=int(input("enter number : "))
if num >= 90:
    print(num,"Grade A")
elif num >= 75:
    print(num,"Grade B")
elif num >= 50:
    print(num,"Grade C")
else:
    print("Fail")

# 4. Leap year 
year = int(input("ENTER YEAR : "))
if year %4==0:
    print(year,": is a Leap year")
else:
    print(year,": is not a Leap year")

# 5. voting eligibility
Age = int(input("enter age : "))
if Age >= 18:
    print("you can vote")
else:
    print("cannot vote")

# 6. car eligibility
age = int(input("enter age : "))
if age >= 18 and age <= 65:
    print("you can drive")
elif age >= 66:
    print("you cannot drive you are senior citizen")
else:
    print("not eligible")

# 7. simple calculator

num1 = int(input("enter number : "))
num2 = int(input("enter number : "))
op = input("enter operator (+,-,*,/): ")
if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)

# 8. triangle validity

angle1=int(input("enter angle1 : "))
angle2=int(input("enter angle2 : "))
angle3=int(input("enter angle3 : "))
result = angle1+angle2+angle3
if result == 180:
    print("this is traingle")
else:
    print("this is not traingle")

# 9. find greatest among 4 numbers 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("Greatest is:", a)
elif b >= a and b >= c and b >= d:
    print("Greatest is:", b)
elif c >= a and c >= b and c >= d:
    print("Greatest is:", c)
else:
    print("Greatest is:", d)






