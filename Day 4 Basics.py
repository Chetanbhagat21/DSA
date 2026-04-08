# string 

s="hello"

# indexing and slicing 

s="python"
print(s[0])
print(s[-1])
print(s[0:3])
print(s[::-1])

# loop through string 
for ch in "hello":
    print(ch)

# important string methods 

s="hello world"
print(s.upper())
print(s.lower())
print(s.count('l'))
print(s.replace("hello","hi"))
print(s.split())


# string is immutable 
# wrong
s="hello"
s[0]="H"    # ERROR   

# correct 
s="hello"
S="H"+s[1:]
print(S)











