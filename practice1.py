print("---------------------sum of the elements in array-----------------------")
def arr():
    arr=[1000000001,1000000002,1000000003,1000000004,1000000005]
    return sum(arr)
print(arr())

print("----------------------diagonal difference ------------------------")
"""a=[
    [1,2,3],
    [4,5,6],
    [9,8,10]
]

1+5+10=16
3+5+9=17
"""
a=[
    [1,2,3],
    [4,5,6],
    [9,8,10]
]
n=3
left=right=0
for i in range(n):
   left+=a[i][i]
   right+=a[i][n-1-i]
print(left,right)

print("------------------------prime numbers-------------------------------")
n=100
prime=[]
notPrime=[]
for i in range(2,n):
    cm=0
    for j in range(2,i):
        if i%j==0:
            cm+=1
        if cm>0:
            break
    if cm==0:
        prime.append(i)
    else:
        notPrime.append(i)
print(prime)
print(notPrime)

print("-------------------------------given an array elements, calculate the fractions of its elements that are positive, negative and are zeros. print the decimal value of each fraction on a newline------------------------------")
arr=[1,1,0,-1,-1]
len=len(arr)
pos=neg=zero=0
for i in arr:
    if i>0:
        pos+=1
    elif i==0:
        zero+=1
    else:
        neg+=1
valPos=pos/len
valNeg=neg/len
valZero=zero/len
print(valPos,valNeg,valZero)
print("---------------------staircase-------------------------")
n=4
for i in range(n,0,-1):
    print(" " *(n-i)+"*"*i)
for i in range(1,n+1):
    print(" " *(n-i)+"*"*i)
    
print("-------------------------min max ---------------------")
"""
 arr=[1,3,5,7,9]
 1+3+5+7=16
 3+5+7+9=24
"""
arr=[1,3,5,7,9]
sum=0
for i in range(4):
    sum+=arr[i]
print(sum)

sum=0
for i in range(1,5):
    sum+=arr[i]
print(sum)

