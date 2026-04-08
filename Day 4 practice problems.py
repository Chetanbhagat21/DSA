"""# 1. Reverse string 

a="hello"
print(a[::-1])

# 2. check palindrome 

b=input("enter text : ")
if b==b[::-1]:
    print(True,"this is palindrome")
else:
    print(False,"this is not palindrome")


# 3. count vowels 

c="python"
count=0
for ch in c:
    if ch in "aeiou":
        count+=1
print(count)

# 4. remove spaces 

d="hello world"
d=d.replace(" ","")
print(d)


e="hello world"
result=""
for ch in e:
    if ch!=" ":
        result+=ch
print(result)
"""
# 5. anagram check 
a="listen"
b="silent"
c=sorted(a)==sorted(b)
print(c)















