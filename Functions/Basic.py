#Create a function to print Hello World
def greet():
    print("Hello World!")
greet()

#Create a function that print name 10 times
def greet():
    for i in range(1,11):
        print("Zahid Khan")
greet()

#Create a function that accepts a name and prints a welcome message
def greet():
    name="Zahid Khan"
    print(f"Welcome {name}")
greet()

#Sum of two numbers using a function
def sum(a,b):
    print(a+b)
sum(10,20)

#Largest of two numbers
def largest(a,b):
    if a>b:
        print(f"{a} is largest")
    else:
        print(f"{b} is largest")
largest(10,20)

#Smallest of three numbers
def smallest(a,b,c):
    if a<b and a<c:
        print(a)
    elif b<a and b<c:
        print(b)
    else:
        print(c)
smallest(100,89,599)

#Check a number is even or odd
def even_odd(num):
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
even_odd(3)
even_odd(10)

#Check a number is positive ,negative or zero
def pnz(num):
    if num>0:
        print(f"{num} is positive")
    elif num<0:
        print(f"{num} is negative")
    else:
        print(f"{num} is zero")
pnz(0)
pnz(20)
pnz(-20)

#Find the square of a number
def square(num):
    print(f"Square of {num} is {num**2}")
square(3)
square(2)

#Find the cube of a number
def cube(num):
    print(f"Cube of {num} is {num**3}")
cube(2)
cube(3)

#Find area of rectangle
def rectangle(l,b):
    print(f"The area of rectange is {l*b}")
rectangle(2,5)
rectangle(5,10)

#Find the perimeter of rectangle
def peri_rect(l,b):
    print(f"The perimeter of a rectangle is {l+b+l+b}")
peri_rect(10,5)

#Find area of circle
def circle(r,PI=3.14):
    print(f"The area of a Circle is {PI*r**2}")
circle(7)

#Convert Celsius to Fahrenheit
def fun(Celsius):
    Fahrenheit=(Celsius*9/5)+32
    print(Fahrenheit)
fun(30)

#Convert Fahrenheit to Celsius
def fun(Fahrenheit):
    Celsius=(Fahrenheit-32)*5/9
    print(Celsius)
fun(30)

#Calculate Simple Interest
def Simple_interest(p,t,r):
    print(f"Simple Intaerst is {(p*t*r)/100}")
Simple_interest(20,2,30)

#Average of N numbers
def Avg(a,b,c,d,e,f):
    Total=a+b+c+d+e+f
    print(f"The Average is {Total/6}")
Avg(23,54,67,89,90,32)

#Max of 5 numbers
def fun(a,b,c,d,e):
    Maximum=a
    if b>Maximum:
        Maximum=b
    if c>Maximum:
        Maximum=c
    if d>Maximum:
        Maximum=d
    if e>Maximum:
        Maximum=e
    print(f"Maximum is {Maximum}")
fun(10,50,89,100,12)

#Swap two numbers
def swap(a,b):
    print(f"Before Swapping a={a} and b={b}")
    a=a+b
    b=a-b
    a=a-b
    print(f"After Swapping a={a} and b={b}") 
swap(10,20)

