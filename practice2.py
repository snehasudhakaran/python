print("--------------------------amstrong number------------------------")
num=156
length=len(str(num))
s=num
result=0
    
while (num!=0):
    div = num%10
    result+=div**length
    num//=10
    
if s==result:
    print("yes its is a amstrong number")
else:
    print("it is not a amstrong number")
    
print("---------------------------pattern------------------------")

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()   
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    
print()
n=5
for i in range(0,n):
    for j in range(i+1):
        if   (i==(n-1) or j==0 or j==i) :
            print("*",end=" ")
        else:
            print(end=" ")
    print()
    
print("--------------factorial--------------------------")

import math
n=5
print(math.factorial(n))

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(n))

sum=1
for i in range(1,n+1):
    sum*=i
print(sum)