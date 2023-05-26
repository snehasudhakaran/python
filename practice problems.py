print("===================find sum of first natural positive integers=======================")
num=100
sum=(num*(num+1))/2
print(int(sum))
num=20
sum=num**2
print(sum)
sum=num*(num+1)
print(sum)

print("===================how to get time of a python program's execution=======================")
import time
def func():
    start_time=time.time()
    s=0
    for i in range(10):
        s+=i
    end_time=time.time()
    return s ,end_time-start_time
print(func())

print("===================How to get the current username in python=======================")
import getpass
print(getpass.getuser())

print("===================How to access environment variables in python=======================")

import os
print(os.environ)
print(os.environ['PATH'])

print("===================How to do a profile python script=======================")
# import cProfile
# def func():
#     print("sneha")
# cProfile.run(func())

print("===================How to list all files of a directory in python =======================")
# from os import listdir
# from os.path import isfile,join
# files_list=[f for f in listdir('/Users') if isfile(join("/Users", f)) ]
# print(files_list)

print("===================How to find out the version of python =======================")
import sys
print(sys.version)
print(sys.version_info)

print("===================How to print current date and time in python =======================")
import datetime
now =datetime.datetime.now()
print(now)
print(now.strftime("%B %A %Y  %H:%M:%S"))

print("===================How to find area of a circle in python =======================")
from math import pi
r=float(5)
print("Area of a circle with radius 5",pi*(r**2))

print("===================How print first and last name in reverse order i python =======================")
first_name = "sneha"
last_name= "sudhakaran"
print(last_name+" "+first_name)

print("===================How to create a list and tuple with comma separated number in python =======================")
# values = input("enter values")
# list = values.split(",")
# tuple =tuple(list)
# print(list)
# print(tuple)

print("===================How to extract extension from filename in python=======================")
filname = "sneha.py"
file = filname.split(".")
print(file[-1])

print("===================Display the first and last colors from a given list =======================")
colors =["orange","violet","purple","blue"]
print("%s %s"%(colors[0],colors[-1]))

print("===================Display a sample examination schedule =======================")
exam_date =(10,8,2023)
print("%i / %i / %i"%(exam_date))

print("===================How to read a number n and nn+nnn =======================")
a=2
first = int("%s"%a)
first1 = int("%s%s%s"%(a,a,a))
first2 = int("%s%s"%(a,a))
print(first+first2+first1)

b=2
b1=b*11
b2=b*111
print(b+b2+b1)

print("===================How to print the documents of python built in function=======================")
print(float.__doc__)
print(int.__doc__)
print(str.__doc__)
print(abs.__doc__)

print("===================How to print a calendar for the given month and year=======================")
import calendar
print(calendar.calendar(2023))
print(calendar.month(2023,5))

print("===================How to write string without having escape =======================")
print("""                 i 
            think
                                    yes""")
print("===================How to calculate no. of days between 2 dates in python =======================")
from datetime import date
first = date(2021,7,8)
first1 = date(2020,7,8)
va = first - first1
print(va.days)
print("===================How to find volume and surface area of sphere in python =======================")
pi = 3.14
r=6
surfaceArea = 4*pi*r*2
v = 4/3 *pi*r*3
print(surfaceArea,v)

print("sneha", "sudhakaran",sep=";")
print("a=10", "b=10",sep=";")
print(ord("a"))
print(chr(67))

print("===================How given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target =======================")

nums=[2,7,11,15]
output=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==9:
            output.append(i)
            output.append(j)
print(output)

nums=[3,2,4]
output=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==6:
            output.append(i)
            output.append(j)
print(output)
print("====================================how to find the difference between two numbers in python==================")
def difference(n):
    if n<17:
        return 17-n
    else:
        return (n-17)*2
print(difference(10))
print("====================================calculate sum of three numbers, if the values are equql the return thrice of their sum in python==================")
def sum(x,y,z):
    sum=x+y+z
    if x==y==z:
        sum = sum*3
    return sum
print(sum(3,3,2))
print("====================================How to get a new string from a given string in python==================")
def new(s):
    if len(s)>2 and s[:2]=="is":
        print(s)
        return s
    return "is"+s
print(new("issneha"))
print("====================================How to find whether an integer is odd or even ==================")
num=31
if num%2==0:
    print("even")
else:
    print("odd")
print("====================================how to reverse a number using slice operations==================")
num=123
print(int(str(num)[::-1]))


print("==============practice===========")
print("hello \nworld \t u")
""" sneha is
good girl"""
x,y,z="moni","sneha","swetha"
like=dislike ="yes"
print(y)
print(like)
print(dislike)

string ="sneha sudhakaran"
string1=string.upper()
string2=string.lower()
string3=string.title()
string4=string.capitalize()
print(string1)
print(string2)
print(string3)
print(string4)
print(string.rfind("a"))
print(string.find("a"))
print(string.find("z"))
print(string.index("a"))
print(string.rindex("a"))
print(string.count("a"))
print(string.replace("a","r"))
print(string.isalpha())
print(string.isdigit())
print(len(string))
otp=2345
print("otp"+str(otp))
name= "Anand"
days =15
year = 2021
print("Dear " + name + ",")
print(f"you have {days} of leave balance for this year ({year}).")

print("===================to get uer input====================")
# Name = input("enter your name")
# Email = input("enter your email address")
# Phone = int(input("phone number please?"))
#
# print(f"UserName: {Name} ")
# print(f"Email: {Email} ")
# print(f"Phone no.: {Phone}")

print("===================how to find the biggest and smallest using list====================")
list =[1,2,4,3,12,4,3,12,45,6,7,8]
print("max",max(list))
print("min",min(list))
print("===================how to calculate the sum of elements in a list in python====================")
# list=[1,2,3,4]
# print("sum",sum(list))

print("=======================how tofind area of triangle===============")
import math
a=float(5)
b=float(4)
c= float(5)
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area %.1f"%area)
print("=======================how tofind area of triangle with given base and height in python===============")
b=float(7)
h=float(8)
area = (b*h)/2
print(area)
print("=======================how to get a string which is n copies of given string in python===============")
def func(string,n):
    # result=""
    # for i in range(n):
    #     result = result+string
    # return result
    print(string*n)
func("sneha " , 4)
func("vik ",3)


print("======================practice through videos=======")
print(round(2.3))
print(round(2.8))
print(abs(-5))
print(pow(2,3))
a=7
b=8
print(max(a,b))
print(min(a,b))
import math
n=5
print(math.log2(n))
print(math.cos(n))
print(math.e**n)

print("=============if else=====================")
pwd_correct=True
if pwd_correct:
    print("true")
else:
    print("false")
num=20
print(num!=20)

string="sneha sudhakaran"
print(string[1:-2])
x=slice(2,-2)
print(string[x])

str="happy"
print(str[0])
print(str[:2])
print(str[:3])
print(str[:4])
print(str[:5])
print(str[-1])
print(str[-2:])
print(str[-3:])
print(str[-4:])
print(str[-5:])

lists=[1,2,3,4]
print(list[0])
lists.append(5)
print(lists)
lists[0]="sneha"
print(lists)
lists.insert(4,"sudhakaran")
print(lists)
print("====================how do you find out if number is odd or even=======")
num=24
if num%2==0:
    print("even")
else:
    print("odd")

print("============how to count the number of items in a list =======")
list =[1,2,3,4,5,6,6,6,6,7,8]
count=0
# for i in range(len(list)):
#     if list.index(list[i]) !=i:
#         count=count+1
# print(count)
for i in list:
    if i==6:
        count=count+1
print(count)
print("============how to find n copies of the first 2 characters of given string =======")

str="s"
flen=2
if flen>len(str):
    flen =len(str)
str=str[:flen]
result =""
for i in range(3):
    result=result+str
print(result)
print("============How to check if item is in list in python=======")
list=[1,2,3,4,5]
val=5
for i in list:
    if i==val:
        print("true")
        break
else:
    print("false")
print("============how to create a histrogram from a given list of integer=======")
list=[3,2,4]

# for i in list:
#     output=""
#     times =i
#     while (times>0):
#         output+="*"
#         times=times-1
#     print(output)
for i in list:
    output=""
    times=i
    while(times>0):
        output+="*"
        times=times-1
    print(output)

list=[1,3,5]
for i in list:
    for j in range(1,i+1):
        print("*",end="")
    print()

# list = list(range(1,20))
# print(list)

#guess the number
import random
# guess=int(input("enter a number"))
# num = random.randint(0,10)
# times=0
# while guess!=num and 4!=times:
#     if num<guess:
#         print("too high")
#     else:
#         print("too low")
#     guess=int(input("enter a number"))
#     times=times+1
# if times==4:
#     print('you lost')
# else:
#     print("won")
#
print("==================break======================")
# list=[]
# while True:
#     inp = input("enter a number, to escape enter z")
#     if inp == "z":
#         break
#     list.append(int(inp))
# print(list)
print("=======================continue==================")
str="A,B,C,D,E"
str2=""
for i in str:
    if i ==",":
        continue
    str2 +=i
print(str2)
print("=======================pass==================")
str2=""
for i in str:
    if i ==",":
        pass
    else:
        str2 =str2+i
print(str2)
print("=================split and join==========")
str="dgh,gh,uiii"
str2=str.split(",")
print(str2)
stre=" ".join(str2)
print(stre)
tuple=(1,2,4)
print(tuple)
tn=[[1,2,3],[2,3,4,5]]
tni = tn[:]
import copy
tnrr=copy.deepcopy(tn)
print(tni)
print(tnrr)
tn[0][0]="sneha"
print(tni)
print(tn)
print(tnrr)

print("====================Assignment===========================")
print("============factors of n===============")
x=14
for i in range(1,x+1):
    if x%i==0:
        print(i)
print("===========to do list =============")

# num= input("enter you to do list with comma separation")
# s = num.split(",")
# print(s)

print("=============peak element==========")
list=[3,4,5,67.9,8]
a=list[0]
for i in list:
    if a<i:
        a=i
print(a)

print("=============move all the negative to end of the list=============")
list=[3,4,5,-2,-1,2,8,0,-4]
list.sort()
list.reverse()
print(list)

n=5
x=20
list=[]
for i in range(1,x+1):
    if x%i==0:
        list.append(i)
        # print(i)
for j in list:
    if j>=n:
        break
    print(j)
print("=============")
str_ip="34,5,2,8,9"
str=[]
for i in str_ip:
    if i==",":
        continue
    str.append(int(i))
print(str)

print("===============how to turn a list into a string========================")
list =["20","40","89"]
copy = "".join(list)
print(copy)

s=""
for i in list:
    s=s+i
print(s)

print("---------------------------------How to print even number in range------------------------------")
for i in range(1,10):
    if i%2==0:
        print(i)
print("----------------------how to compare list in python?--------------------------------")
c1 =set(["white", "black","orange"])
c2 = set(["white","black","violet"])
compare = c1.difference(c2)
print(compare)

print("---------------------how to find the greatest common factor / hcf -----------------------------")
n1=18
n2 =16
if n1>n2:
    small =n2
else:
    small= n1
while  small>=2 :
    if n1%small==0 and n2% small==0:
        print("HCF" ,small)
    small = small-1
print("---------------------how to find the lcm -----------------------------")
n1=7
n2=8
if n1>n2:
    high=n1
else:
    high=n2
value = high
while True :
    if high%n1==0 and high %n2==0:
        print("lcm", high)
        break
    else:
        high=high+value
dict={
    "name":"sneha",
    "age":78
}
for keys in sorted(dict.keys()):
    print(keys)
print("***{msg:^50}***".format(msg="message"))
print("{:e}".format(6))

def func(a):
    a.sort()
    print(a)
a=[1,2,34,6]
func(a[:])
print(a)

print("--------------------add names -----------------------")
dict ={
    "name":["sneha","vikram","sudhakaran","noorul","moni"],
    "fav":["chappati","kuruma","chocolate","icecream","briyani"]
}
dict["fav"].sort()
print(dict)

print("--------------------How to sum of three given integers -----------------------")
def sum(x,y,z):
    sum=x+y+z
    return sum
print(sum(3,4,5))

print("--------------------How to sum of 2 given numbers and return a number -----------------------")

def sum(x,y):
    sum=x+y
    return sum
print(sum(5,6))
print("--------------------How to add two objects if both objects are an integer type in python -----------------------")
def add(x,y):
    if not (isinstance(x, int) and isinstance(y,int)):
        raise TypeError("it  must be integer")
    return x+y
print(add(4,7))
print("--------------------How to display name, age, address in three different lines -----------------------")
name="sneha"
age=21
address="3/441"
print(f"name: {name} \nage: {age} \naddress: {address}")
print("--------------------How to solve {x*y}*{x+y} -----------------------")
x=3
y=7
print((x*y)*(x+y))
print((x*x*y)+(y*y*x))

print('------------------------write a function to list the first N prime numbers------------------------')

# for i in range(2,20):
    # for j in range(2,i):
    #     if i%j==0:
    #         continue
    #     print()
            
print('---------------------write a function to sort a list of values--------------------')
list=[5,3,2,4,1,6]

for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i]<=list[j]:
            list[i],list[j]=list[j],list[i]
print(list)
        # print(list)
print('-------------------reverse-----------------------')
start=3
end=7
sneha=[10,20,30,40,50,60,70,80,90,100]     
def sneha1(start,end,sneha):
    while start<end:
        sneha[start],sneha[end]= sneha[end],sneha[start]
        start+=1
        end-=1
    return sneha
print(sneha1(start,end, sneha))
print("-----------------------------linear quation in two variables--------------------------")
import numpy as np
# a=5x+3y =35
# x+y = 9
'''
  a=[
      [5,3],
      [1,1]
  ]
  b=[35,9]
'''
A=[[5,3],[1,1]]
B=[35,9]
x= np.linalg.solve(A,B)
print(x)

#5x+3y=35
for x in range(1,6):
    for y in range(1,11):
        if 5*x + 3*y==35:
            print("x",x,"y",y)
#x+y=9

for x in range(1,8):
    for y in range(1,9):
        if x+y==9:
            print("x",x,"y",y)
print('-------------------------------tic tac toe game--------------------')   
board=[
    [2,1,2],
    [0,0,2],
    [2,0,2]
]        
def check(player):
    
    for row in board:
        if row.count(player)==3:
            return True
    s=[0,1,3]
    for col in s:
        if board[0][col]==player and board[1][col] and board[2][col]:
            return True
        if board[0][0]==player and board[1][1] and board[2][1]:
            return True
        if board[0][2]==player and board[1][1] and board[2][0]:
            return True
        return False
if check(1):
    print("1 won")
elif check(2):
    print("2 won")
elif check(0):
    print("no one own")
else:
    print("wrong")


print('------------------------------gcd-------------------------')
def gcd(a,b):
    if b==0:
        return a 
    else: 
        return (gcd(b,a%b))
GCD =gcd(12,16)
print(GCD)

n1=8
n2 =7
if n1>n2:
    small =n2
else:
    small= n1
while  small>=1 :
    if n1%small==0 and n2% small==0:
        print("HCF" ,small)
    small = small-1
    
print("---------------------lcm---------------------")
n1=2
n2=4
if n1>n2:
    high=n1
else:
    high=n2
value = high
while True :
    if high%n1==0 and high %n2==0:
        print("lcm", high)
        break
    else:
        high=high+value
print('------------------------how to compute the future value of rate of interest and  a number of years in python----------------')
amt=10000
int=3.6
years=7
interest= amt*((1+(0.01*int))**years)
print(round(interest))
print("-----------------------------compare the triplets---------------")
a=[2,4,6,8,2]
b=[3,7,1,4,1]
alice=bob=0
for i in range(len(a)):
    if a[i]>b[i]:
        alice+=1
    else:
        bob+=1
print(alice, bob)
print("-----------------------write a function to multiply two matrics-----------------")
a=[
    [1,2,4],
    [4,5,4],
    [6,7,8]
]
b=[
    [3,4,4],
    [4,6,4],
    [6,7,8]
]
c=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j]+=a[i][k]*b[k][j]
print(c)

print("------------------------------addition and sub for two matrix--------------------")
a=[[1,2],[3,5]]
b=[[4,2],[5,3]]
c=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]+=a[i][j] +b[i][j]
print(c)

a=[[1,2],[3,5]]
b=[[4,2],[5,3]]
c=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]+=a[i][j] -b[i][j]
print(c)

print("-------------------------file handling-----------------------")
# with open("python.txt","a+") as f:
#     f.seek(0)
#     s=f.read()
#     ss= s.replace("cows","ducks")
#     mm =ss.replace("moo","qucks")
#     f.write(mm)
# n=23.4555
# print("%3.1f"%n)

print("-------------------------brithday------------------------------------")
arr=[1,3,2,5,4,5,5]
def brithDayCandles(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>=arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    max=arr[-1]
    return arr.count(max)
print(brithDayCandles(arr))

print("----------------------------gcd and coprime---------------------------")
a=3
b=5
def gcd(a,b):
    if b==0:
        return a 
    else:
        return gcd(b,a%b)
    
    
if gcd(a,b)==1:
    print(a,b,"are coprime")
else:
    print(a,b,"are not coprime")
    
print(gcd(3,5))

print(math.gcd(8,2))

print("--------------------guess the output----------------")
p=(1,3)
q=0
r=[]

if p or q and r :
    print("true")
else:
    print("false")
    
print("-------------sort--------------------")

arr=[1,2,5,2,5,6,9,2,15,23,56,1,2,3]


for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>=arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
            
print(arr)

print("--------------------------------")

arr=["abc","123"]

# for i in arr:
#     print(i)
#     arr.append(i)
# print(arr)

print("------------------------leap year----------------------------")
year=2001
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("it's leap year")
        else:
            print("it;s not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")

print("---------------------how to find -ve and +ve------------------------")

n=-5
if n>0:
    print("positive")
elif n==0:
    print("neither +ve nor -ve")
else:
    print("-ve")
    
print("--------------------------------------------------------")
arr=[4,29,9,7,1,3,9,7]
k=4

arr.sort()
for i in range(k-1):
    arr.remove(max(arr))
print(max(arr))

print("-----------------------captial index-------------------------------------")
up=[]
def captial_index(x):
    for i in range(len(x)):
        if x[i].isupper():
            up.append(i)
captial_index("HeLlO")
print(up)

print("--------------middle letter-------------------------------")

def middle(x):
    mid=len(x)//2
    if len(x)%2==0:
        return "*"
    else:
        return x[mid]
print(middle("sneh"))

print("-----------------------------lambda--------------------------------")

x= lambda a : a+2 
print(x(6))

print("----------------------------walrus operator----------------------------------")
print(name:="sneha")

# up=[]
# while not (inpt:=input("enter num")) == "z" :
#     up.append(inpt)
# print(up)

print("---------higher order functions--------------------")
def cal_down():
    print("calm down")
    
def happy():
    print("happy")
    
def sad():
    print("crying")
    
def feeling(func):
    func()
    cal_down()
    
feeling(happy)
feeling(sad)
joy=happy
joy()

print("-----------------------------------------sort------------------------------")

items=[(3456,"shoes",780),(3566,"phone",2500),(2587,"book",450),(544712,"pen",75)]
items1=sorted(items,key=lambda items:items[1])
print(items1)

    
print("---------------higher order function---------------------------------")
print("---------------------matrix add sub mul-----------------------------")

a=[[1,2],[3,4]]
b=[[2,1],[2,6]]

c=[[0,0],[0,0]]

for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]+=a[i][j]+b[i][j]
print(c)

a=[[1,2],[3,4]]
b=[[2,1],[2,6]]

c=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=a[i][j]-b[j][i]
print(c)

a=[[1,2],[3,4]]
b=[[2,1],[2,6]]

c=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j]+=a[i][k] * b[k][j]
            
print(c)

print("------------------------------matrix transpose------------------------")
a=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
b=[
    [10,11,12],
    [13,14,15],
    [16,17,18]
]
c=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(len(a)):
    for j in range(len(a)):
        a[i][j]=a[j][i]
        
print(a)

print("-----------------------bubble sorting----------------------------------")

array=[3,6,2,16,42,1,3,5,4]

for i in range(0,len(array)):
    for j in range(i+1,len(array)):
        if array[i]>array[j]:
            array[i], array[j]=array[j],array[i]
print(array)
print("---------------validate date-----------------------")
month=12
day=33
year=2014

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    max_days=31
elif month==11 or month==4 or month==6 or month==9 :
    max_days=30
elif year%4==0 and year%100!=0 or year%400==0:
    max_days=29
else:
    max_days=28
    
if month<1 or month>12:
    print("invalid month")
elif day<1 or day>max_days:
    print("invalid day")
else:
    print("valid date")
    
print("-----------------------flames--------------")

name1="Sneha"
name2=" vikram"

name1=name1.lower().replace(" ","")
name2=name2.lower().replace(" ","")

print(name1)
print(name2)

for i in name1:
    for j in name2:
        if i==j:
            name1=name1.replace(j,"")
            name2=name2.replace(j,"")
            
print(name1)
print(name2)

join = len(name1)+len(name2)
print(join)

print("------------------------------characters--------------------")

string="Sneha Sudhakaran is girl"

n=4
if n==1:
    print(string.upper())
elif n==2:
    print(string.lower())
elif n==3:
    print(string.capitalize())
elif n==4:
    print(string.title())
elif n==5:
    print(string.swapcase())
    
n=5

for i in range(n):
    # k=ord("A")+i
    k=ord("A")+i
    for j in range(i+1):
        print(chr(k),end=" ")
        # k=k+1
    print()
    
print("------------------------practice------------------------------")
list1={"name":"sneha","age":20,"clg":"Dr. MGR"}
dict={key:val for key,val in list1.items()}
print(dict)
        
print(list1 is not dict)

# items=("phone","tv")
# price=(25000,30000)
# dj=list(zip(items,price))
# print(dj)

print("------------------multithreading----------------------------")
# import threading
# import time
# print(threading.active_count())
# print(threading.enumerate())

# def update():
#     print("updating")
#     time.sleep(9)
#     print("updated")

# threadd= threading.Thread(target=update)
# threadd.start()
# for i in range(100):
#     print(i)
# threadd.join()
# print("bye")

print("------------------------patterns---------------------------")

n=7
s=[k for k in range(1,8)]
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print(s[j],end="")
        else:
            print(" ",end="")
    print()
# 

