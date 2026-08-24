#Check even or odd
num=int(input("Enter a number:"))
if(num%2==0):
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")    

#Check the number is positive or negative
num=int(input("Enter the number:"))
if(num>0):
    print(f"{num} Positive Number")
else:
    print(f"{num} Negative Number")    

#Elgible for vote
Age=int(input("Enter your Age:"))
if(Age>=18):
    print("You are elgible for voting")
else:
    print("Not elgible for voting")    

#Pass or Fail
Marks=int(input("Enter your Marks:"))
if(Marks>=35):
    print("Pass")
else:
    print("Fail")

#Adult or Minor
Age=int(input("Enter your:"))
if(Age>=18):
    print("Adult")
else:
    print("Minor")

#Greater of two numbers
a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
if(a>b):
    print("A is greater then B")
else:
    print("B is greater than A")


#Smaller of two numbers
a=int(input("Enter the first Value:"))
b=int(input("Enter the second value:"))
if(a<b):
    print("A is smaller than B")
else:
    print("B is smaller than A")

#Eligible for driving licence
Age=int(input("Enter your Age:"))
if(Age>=18):
    print("Eligible for driving licence")
else:
    print("Not Eligible")

#Login successful or failed
Email=input("Enter your Emial:")
Password=int(input("Enter your passowrd:"))
if(Email=="khanzahid2223@gmail.com" and Password==2223):
    print("Login Successful")
else:
    print("Login Failed")

#Correct Password or wrong Password
Password=int(input("Enter your Password:"))
if(Password=="2223"):
    print("Valid Password")
else:
    print("Invalid Password")

#Eligible for Scholership
Percentege=int(input("Enter your Percentage:"))
if(Percentege>=85):
    print("Eligible for Scholership")
else:
    print("Not eligible")

#Rich or poor based on salary
Salary=int(input("ENter your Salary:"))
if(Salary>=50000):
    print("Rich")
else:
    print("Poor")

#Eligible for GYM
Age=int(input("Enter your Age:"))
if(Age>=15):
    print("Eligible for GYM")
else:
    print("Not Eligible")

#Internet connected or disconnected
Internet=input("Can u see your social media is working Yes/No:")
if(Internet=="Yes"):
    print("Internet is Connected")
else:
    print("Internet is not connected")

#Battery is low or sufficient
Battery=int(input("What is your Battery Percentege:"))
if(Battery>=20):
    print("Battery is Sufficient")
else:
    print("Battery is low")

#Number divisible by 5 or not
num=int(input("Enter the number:"))
if(num%5==0):
    print(f"{num} is divisible by 5")
else:
    print(f"{num} is not divisible by 5")

#Number is divisible by 10 or not
num=int(input("Enter the number:"))
if(num%10==0):
    print(f"{num} id divisible by 10")
else:
    print(f"{num} id not divisible by 10")

#Student Present or Absent
Stundent=input("Is Student is Present or Absent:")
if(Stundent=="Yes"):
    print("Student is Present")
else:
    print("Student is Absent")

#Product in stock or out of stock
Product=input("Is the Product is avaliable:")
if(Product=="Yes"):
    print("Product in Stock")
else:
    print("Product is out of stock")

#Namaz is farz if agr is greater than 15
Age=int(input("Enter your age:"))
if(Age>=15):
    print("Namaz is Farz on you")
else:
    print("Tu abhi baccha hai")