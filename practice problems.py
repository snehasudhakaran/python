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
        high=high+1
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
