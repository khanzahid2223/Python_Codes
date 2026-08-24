#Return square of a number
def square(num):
    return num**2
print(square(2))

#Return the factorial
def factorial(num):
    fact=1
    for i in range(1,num+1):
            fact=fact*i
    return fact
print(factorial(5))

#Return wheather the number is prime
def fun(num):
    Count=0
    for i in range(1,num+1):
        if num%i==0:
            Count+=1
    if Count==2:
        return True
    return False
print(fun(10))

#Palindrome
def fun(num):
    Rev=0
    Org=num
    Count=len(str(num))
    for i in range(Count):
        LD=num%10
        Rev=Rev*10+LD
        num=num//10
    if Org==Rev:
        return True
    return False
print(fun(121))
print(fun(12321))
print(fun(1210))

#Armstrong Number
def Arm(num):
    Count=len(str(num))
    Org=num
    Sum=0
    for i in range(Count):
        LD=num%10
        Sum=Sum+(LD**Count)
        num=num//10
    if Org==Sum:
        return True
    return False
print(Arm(153))

#Reverse a Number
def rev(num):
    Rev=0
    Org=num
    Count=len(str(num))
    for i in range(Count):
        LD=num%10
        Rev=Rev*10+LD
        num=num//10
    return Rev
print(rev(2223))

#Sum of digits
def sum(num):
    Sum=0
    Count=len(str(num))
    for i in range(Count):
        LD=num%10
        Sum=Sum+LD
        num=num//10
    return Sum
print(sum(555))

#Count of digits
def count(num):
    Count=0
    c=len(str(num))
    for i in range(c):
        LD=num%10
        Count+=1
        num=num//10
    return Count
print(count(1234567890))

#Largest Digit
def large(num):
    Largest=0
    Count=len(str(num))
    for i in range(Count):
        LD=num%10
        if LD>Largest:
            Largest=LD
        num=num//10
    return Largest
print(large(23469896432542))

#Smallest Digit
def small(num):
    Smallest=int(input("Entar a number:"))
    Count=len(str(num))
    for i in range(Count):
        LD=num%10
        if LD<Smallest:
            Smallest=LD
        num=num//10
    return Smallest
print(small(123345))

#Prodect of Digits
def prod(num):
    Prodect=1
    Count=len(str(num))
    for i in range(Count):
        LD=num%10
        Prodect=Prodect*LD
        num=num//10
    return Prodect
print(prod(524))

#First Digit
def last_digit(num):
    Count=len(str(num))
    for i in range(Count):
        LD=num%10
        num=num//10
    return LD
print(last_digit(82))

#Last Digit
def first_digit(num):
    Count=len(str(num))
    for i in range(Count):
        LD=num%10
    return LD
print(first_digit(12345))


# Digital Root(5+5=10->1+0=1)
def sum_of_digits(num):
    Sum = 0
    while num > 0:
        LD = num % 10
        Sum = Sum + LD
        num = num // 10
    return Sum


def Digital_root(num):
    Sum = sum_of_digits(num)
    while Sum > 9:
        Sum = sum_of_digits(Sum)
    return Sum




