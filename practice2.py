if __name__ =="__main__":
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
                print("*",end="")
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

    print("----------------------------------pattern----------------------")

    n=5
    for i in range (5,0,-1):
        print(" "*(n-i) + "*"*i)
        
    print()

    for i in range(n):
        for j in range(n):
            if (i==0) or (i==j) or (j==(n-1)):
                print("*",end="")
            else:
                print(end=" ")
        print()
    print("---------------------------fibonacci----------------------------")
    n=4
    def fab(n):
        a=0
        b=1
        if n==0:
            print(a)
        elif n==1:
            print(a)
            print(b)
        else:
            print(a,end=" ")
            print(b , end=" ")
            for i in range(1,n):
                c=a+b
                a=b
                b=c
                print(c,end=" ")
    fab(n)       

    print("---------------prime number------------------------")

    n=1311
    for i in range(2,n):
        if n%i==0:
            print("not a prime")
            break
    else:
        print("prime")

    print("-----------------------perfect numbers positive integers equal to sum of positive divisor excluding the number itself-----------------------------")

    n=7
    result=0
    for i in range(1,n):
        if n%i==0:
            result+=i
    print(result)
    print(result==n)

    print("--------------------------------1234 = 1+2+3+4=10------------------------")
    n=123467
    result=0
    while (n!=0):
        digit=n%10
        result+=digit
        n=n//10
    print(result)

    print("-----------------------palindromic prime numbers--------------------------")
    n=173
    num=n
    result=0
    while(n!=0):
        digit=n%10
        result=(result*10)+digit
        n=n//10
    if num==result:
        for i in range(2,num):
            if num%i==0:
                print("palindromic but not a prime")
                break
        else:
            print("palindromic and prime")
    else:
        for i in range(2,num):
            if num%i==0:
                print("not palindromic but not a prime")
                break
        else:
            print("not palindromic but prime")
            
    print("------------------vowels count---------------------------------")

    list1=["a","e","i","o","u"]
    string="sneha sudhakaran"


    count=0
    for char in string:
        if char in list1:
            count+=1
    print(count)

    print("-----------------------------anagram------------------------------")
    str1="earth"
    str2="Heartg"

    if sorted(str1.lower()) == sorted(str2.lower()):
        print("anagram")
    else:
        print("no it's not a anagram")
        
    print("--------------------------binary search--------------------")

    list1=[2,3,5,1,5,2,6,3,2]
    list1.sort()

    low=0
    high=len(list1)-1
    Found=False

    key=8

    while low<=high and not Found:
        
        mid = (low+high)//2
        if key==list1[mid]:
            Found=True
        elif key>=list1[mid]:
            low=mid+1
        else:
            high=mid-1

    if Found==True:
        print("founded")
    else:
        print("nope")


    print("object oriented programming")

    class vehicle():
        def __init__(self,name,age):
            self.name=name
            self.age=age
        def get(self):
            print("hi",self.name)
    class car(vehicle):
        def __init__(self,name,age,pwd):
            super().__init__(name, age)
            self.pwd=pwd
            self.color=None
            super().get()
            print("hi", self.name,self.age,self.pwd,self.color)
    car1=car("jd",20,123)       
    car2 = car("sd",33,455)

    def set(obj,color):
        obj.color=color
        obj.get()   #duck typing importance to methods rather than objects
    set(car1,"black")
    set(car2,"blue")

    print(car1.color)


    print("-----------------------------------")

    class user():
        def __init__(self,name,age,pwd):
            self.name=name
            self.age=age
            self.pwd = pwd
        def set(self):
            print("hi user" ,self.name)
            
    class student(user):
        def __init__(self,name,age,pwd,year,course):
            super().__init__(name,age,pwd)
            self.year = year
            self.course = course
            super().set()
            
        def set(self):
            print("hi user student", self.name)

    class faculty(user):
        def __init__(self,name,age,pwd,specifications):
            super().__init__(name,age,pwd)
            self.specifications=specifications
            super().set()
            
        def set(self):
            print("hi teacher",self.name,self.specifications)
            
    class st1():
        def __init__(self,__name,age):
            self.__name=__name #dunder variable
            self.age=age
        def __set(self): #dunder method
            print("hi student", self.__name)

    st11=st1("sneha",21)
    print(st11._st1__name)
    st11._st1__set()
    # class st2():
    #     def __init__(self,name,age):
    #         self.name=name
    #         self.age=age
    #         super().set()
    #     def set(self):
    #         print("hi stud2", self.name)
            
    # class facultyStuent(st2,st1):
    #     def __init__(self,name,age):
    #         super().__init__(name,age)
    #         super().set()
            
            
    #     def set(self):
    #         print("hi student facultyschool",self.name,self.age,self.school)

    # user1=user("radha",23,554)     
    # student1=student("sneha",21,12,2022,"btech")
    # faculty1=faculty("sithra",34,454,"BA English")
    # facultyStuent1=facultyStuent("sne",45)

    # user1.set()
    # student1.set()
    # faculty1.set()
                
    print("------------------------------------abstract------------------------")
    from abc import ABC,abstractmethod

    class vehicle(ABC):
        
        def __init__(self,name):
            self.name=name 
        
        @abstractmethod
        def start(self):
            pass
        @abstractmethod
        def stop(Self):
            pass

    class car(vehicle):
        
        def __init__(self,name):
            super().__init__(name)
        
        def start(self):
            print("car",self.name,"started")
        def stop(self):
            print("car stop")
            
    class bike(vehicle):
        def __init__(self,name):
            super().__init__(name)
        def start(self):
            print("bike",self.name,"started")
        def stop(self):
            print("bike stop")
            
            
    bike1=bike("honda")

    car1=car("bmw")

    bike1.start()
    car1.start()

    bike1.stop()
    car1.stop()

def nm():
    print(__name__)

