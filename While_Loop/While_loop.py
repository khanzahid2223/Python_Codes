# #Print number from 1 to 10
# i=1
# while i<=10:
#     print(i)
#     i+=1

# #Print number from 10 to 1
# i=10
# while i>=1:
#     print(i)
#     i-=1

# #Print even number from 1 to 100
# i=1
# while i<=100:
#     if(i%2==0):
#         print(i)
#     i+=1

# #Print odd number from 1 to 100
# i=1
# while i<=100:
#     if(i%2==1):
#         print(i)
#     i+=1

# #Multiples of 5 up to 100
# i=1
# while i<=100:
#     if(i%5==0):
#         print(i,end=" ")
#     i+=1

# #Print Multiplicatin table of a number
# num=int(input("Enter a number="))
# i=1
# while i<=10:
#     print(f"{num}x{i}={num*i}")
#     i+=1

# #Sum of n numbers
# n=int(input("Enter a number="))
# i=1
# Total=0
# while i<=n:
#     Total=Total+i
#     i+=1
# print(f"Total of n is={Total}")

# #Find sum of even numbers till n
# n=int(input("Enter a number="))
# i=1
# Total=0
# while i<=n:
#     if(i%2==0):
#         Total=Total+i
#         print(f"The enen numbers are:{i}")
#     i+=1
# print(f"The sum of even numbers till n is={Total}")

# #Find sum of odd numbers till n
# n=int(input("Enter a number="))
# i=1
# Total=0
# while i<=n:
#     if(i%2==1):
#         Total=Total+i
#     i+=1
# print(f"The sum of odd numbers till n is={Total}",end=" ")

# #Factorial of a number
# num=int(input("Enter a number="))
# Fact=1
# i=1
# while i<=num:
#     Fact=Fact*i
#     i+=1
# print(f"The Factorial of {num} is={Fact}")

# #Count the digits of a number
# num=int(input("Enter a number:"))
# Count=0
# while num>0:
#     Count+=1
#     num=num//10
# print(f"The total number of digits are:{Count}")

# #Reverse a number
# Num=int(input("Enter a numner="))
# Rev=0
# while Num>0:
#     Last_Digit=Num%10
#     Rev=Rev*10+Last_Digit
#     Num=Num//10
# print(f"The Reverse Digit is:{Rev}")

# #Sum of Digits
# Num=int(input("Enter a number="))
# Sum=0
# while Num>0:
#     Last_Digit=Num%10
#     Sum=Sum+Last_Digit
#     Num=Num//10
# print(f"The Sum of digits are:{Sum}")

# #Check for palindrom
# Num=int(input("Enter a number="))
# Orginal=Num
# Rev=0
# while Num>0:
#     Last_Digit=Num%10
#     Rev=Rev*10+Last_Digit
#     Num=Num//10
# if(Orginal==Rev):
#     print(f"{Orginal} is Palindrom")
# else:
#     print(f"{Orginal} is not Palindrom")

# #Armstrong Number
# Num=int(input("Enter a number="))
# Orginal=Num
# Sum=0
# Count=len(str(Num))
# while Num>0:
#     Last_Digit=Num%10
#     Cube=Last_Digit**Count
#     Sum=Sum+Cube
#     Num=Num//10
# if(Orginal==Sum):
#     print(f"{Orginal} is a Armstrong number")
# else:
#     print(f"{Orginal} is not a Armstrong number")

# #Strong Number
# Num=int(input("Enter a number="))
# Orginal=Num
# Sum=0
# while Num>0:
#     Last_Digit=Num%10
#     Temp=Last_Digit
#     Fact=1
#     while Temp>0:
#         Fact=Fact*Temp
#         Temp-=1
#     Sum=Sum+Fact
#     Num=Num//10
# if(Orginal==Sum):
#     print(f"{Orginal} is Strong Number")
# else:
#     print(f"{Orginal} is not a Strong Number")

# # #Number Positive Or Negative
# N=int(input("How Much the number should repeat:"))
# Count=1
# while Count<=N:
#     Num=int(input("Enter a number:"))
#     if(Num>0):
#         print("Positive Number")
#     elif(Num<0):
#         print("Negative Number")
#     else:
#         print("Number is Zero")
#     Count+=1

# #Check the number is Even or Odd
# Repeat=int(input("How many times the loop should repeat:"))
# Count=1
# while Count<=Repeat:
#     Num=int(input("Enter the number to chect even or odd:"))
#     if(Num%2==0):
#         print(f"{Num} is Even Number")
#     else:
#         print(f"{Num} is Odd Number")
#     Count+=1

# #Largest among two numbers
# Repeat=int(input("How many times the loop should repeat:"))
# Count=1
# while Count<=Repeat:
#     Num1=int(input("Enter the first number:"))
#     Num2=int(input("Enter the second number:"))
#     if(Num1>Num2):
#         print(f"{Num1} is largest")
#     else:
#         print(f"{Num2} is largest")
#     Count+=1

# #Largest Among three numbers
# Repeat=int(input("How many times the loop should repeat:"))
# Count=1
# while Count<=Repeat:
#     Num1=int(input("Enter the first number:"))
#     Num2=int(input("Enter the second number:"))
#     Num3=int(input("Enter the third number:"))
#     if(Num1>Num2 and Num1>Num3):
#         print(f"{Num1} is largest")
#     elif(Num2>Num3):
#         print(f"{Num2} is largest")
#     else:
#         print(f"{Num3} is largest")
#     Count+=1

# #Smallest Among three numbers
# Repeat=int(input("How many times the loop should repeat:"))
# Count=1
# while Count<=Repeat:
#     Num1=int(input("Enter the first number:"))
#     Num2=int(input("Enter the second number:"))
#     Num3=int(input("Enter the third number:"))
#     if(Num1<Num2 and Num1<Num3):
#         print(f"{Num1} is smallest")
#     elif(Num2<Num3):
#         print(f"{Num2} is smallest")
#     else:
#         print(f"{Num3} is smallest")
#     Count+=1

# #Check leap year
# Repeat=int(input("How many times the loop should repeat:"))
# Count=1
# while Count<=Repeat:
#     Year=int(input("Enter the year to check leap year or not:"))
#     if((Year%4==0 and Year%100!=0) or (Year%400==0)):
#         print(f"{Year} is leap year")
#     else:
#         print(f"{Year} is not leap year")
#     Count+=1

# #Number is divisible by both 3 and 5
# Repeat=int(input("How many times the loop should repeat:"))
# Count=1
# while Count<=Repeat:
#     Num=int(input("Enter a number:"))
#     if(Num%3==0 and Num%5==0):
#         print(f"{Num} is divisible by both 3 and 5")
#     else:
#         print(f"{Num} is not divisible by 3 and 5")
#     Count+=1

# #Print all the even numbers from A to Z
# Num=int(input("Enter a number:"))
# while Num<=26:
#     if(Num%2==0):
#         print(f"{Num} is even")
#     Num+=1
    
# #Print all odd numbers from A to Z
# Str_Num=int(input("Enter a number:"))
# while Str_Num<=26:
#     if(Str_Num%2!=0):
#         print(f"{Str_Num} is odd number")
#     Str_Num+=1

# #Print number divisible by both 3 and 7
# Count=1
# while Count<=1:
#     Num=int(input("Enter a number:"))
#     if(Num%3==0 and Num%7==0):
#         print(f"{Num} is divisible by both 3 and 7")
#     else:
#         print(f"{Num} is not divisible by 3 and 7")
#     Count+=1

# #Count Even digits in a number
# Count=0
# Num=int(input("Enter a number:"))
# Orginal=Num
# while Num>0:
#     Last_Digit=Num%10
#     if(Last_Digit%2==0):
#         Count=Count+1
#     Num=Num//10
# print(f"{Orginal} has {Count} digits")
    
# #Count the odd digits in a number
# Count=0
# Num=int(input("Enter a number:"))
# Orginal=Num
# while Num>0:
#     Last_Digit=Num%10
#     if(Last_Digit%2!=0):
#         Count+=1
#     Num=Num//10
# print(f"{Orginal} has {Count} odd digits ")

# #Find largest digit in a number
# Largest=0
# Num=int(input("Enter a number:"))
# while Num>0:
#     Last_Digit=Num%10
#     if(Last_Digit>Largest):
#         Largest=Last_Digit
#     Num=Num//10
# print(f"Largest Digit is {Largest}")
     
# #Smallest digit in a number
# Num=int(input("Enter a number:"))
# Smallest=Num
# while Num>0:
#     Last_Digit=Num%10
#     if(Last_Digit<Smallest):
#         Smallest=Last_Digit
#     Num=Num//10
# print(f"The Smallest digit is {Smallest}")

# #Count Zeros in a number
# Count=0
# Num=int(input("Enter a number:"))
# while Num>0:
#     Last_Digit=Num%10
#     if(Last_Digit==0):
#         Count+=1
#     Num=Num//10
# print(f"There are {Count} Zeros in a number")

# #Armstrong Numbers
# Num=int(input("Enter a Number="))
# Original=Num
# Count=len(str(Num))
# Sum=0
# while Num>0:
#     Last_Digit=Num%10
#     Sum=Sum+(Last_Digit**Count)
#     Num=Num//10
# if(Original==Sum):
#     print(f"{Original} is Armstrong Number")
# else:
#     print(f"{Original} is not a Armstrong Number")

# #Strong Number
# Num=int(input("Enter a number="))
# Original=Num
# Sum=0
# while Num>0:
#     Last_Digit=Num%10
#     Temp=Last_Digit
#     Fact=1
#     while Temp>0:
#         Fact=Fact*Temp
#         Temp=Temp-1
#     Sum=Sum+Fact
#     Num=Num//10
# if(Original==Sum):
#     print(f"{Original} is a Strong Number")
# else:
#     print(f"{Original} is not a Strong Number")

# #Perfect Number
# Num=int(input("Enter a number="))
# Diviser=1
# Sum=0
# while Diviser<Num:
#     if(Num%Diviser==0):
#         Sum=Sum+Diviser
#     Diviser=Diviser+1
# if(Sum==Num):
#     print(f"{Num} is a Perfect Number")
# else:
#     print(f"{Num} is not a Perfect Number")

# #Prime Number
# Num=int(input("Enter a Number="))
# Diviser=2
# Prime=True
# while Diviser<Num:
#     if(Num%Diviser==0):
#         Prime=False
#     Diviser+=1
# if(Prime==True):
#     print(f"{Num} is a Prime Number")
# else:
#     print(f"{Num} is not a Prime Number")
    
# #Fibonacci Seriese
# Num=int(input("Enter a Number="))
# First=0
# Second=1
# Count=1
# while Count<=Num:
#     print(First,end=" ")
#     Next=First+Second
#     First=Second
#     Second=Next
#     Count+=1

# #GCD 
# Num1=int(input("Enter the first number="))
# Num2=int(input("Enter the second number="))
# Diviser=1
# GCD=0
# while Diviser<=Num1:
#     if(Num1%Diviser==0 and Num2%Diviser==0):
#         GCD=Diviser
#     Diviser=Diviser+1
# print(f"GCD of a given number is {GCD}")

# #Power Without using **
# Base=int(input("Enter a base value="))
# Power=int(input("Enter a power value="))
# Result=1
# Count=1
# while Count<=Power:
#     Result=Result*Base
#     Count+=1
# print(f"Result for a given number is {Result}")
