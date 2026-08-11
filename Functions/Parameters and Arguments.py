# #Pass makrs of 5 subjects abd calculate total
# def Marks(AI,ADA,Python,CCN,DBMS):
#     total=AI+ADA+Python+CCN+DBMS
#     return total
# print(Marks(90,99,100,78,98))

# #Pass marks and calculate percentage
# def Marks(AI,ADA,Python,CCN,DBMS):
#     total=AI+ADA+Python+CCN+DBMS
#     return total/500*100
# print(Marks(90,99,100,78,98))   

# #Pass salary and calculate HRS
# def Salaray(num):
#     Salaray=num*20/100
#     return Salaray
# print(Salaray(30000))

# #Pass age and check i aperson is eligible for voting
# def Vote(Age):
#     if Age>=18:
#         return True
#     return False
# print(Vote(23))
# print(Vote(12))

# #Pass username and password for login validation
# def log_valid(username,password):
#     if username=="Zahid" and password==2223:
#         return True
#     return False
# print(log_valid("Zahid",2223))

# #Pass two number and return the bigger
# def bigger(num1,num2):
#     if num1>num2:
#         return num1
#     return num2
# print(bigger(20,30))

# #Pass three numbers and return the middel value
# def middle(num1,num2,num3):
#     return num2
# print(middle(23,56,89))

# #Simple Interest
# def Simple_interest(p,r,t):
#     SI=(p*r*t)/100
#     return SI
# print(Simple_interest(2000,20,2))

# #Pass radius and return area of a circle
# def Circle(radius):
#     Circle=3.14*radius**2
#     return Circle
# print(Circle(5))

# #Pass length and breadth and return area of rectangle
# def Rect(length,breadth):
#     Rectangle=length*breadth
#     return Rectangle
# print(Rect(5,10))

# #Pass num and check divisible by 5 and 11
# def div(num):
#     if num%5==0 and num%11==0:
#         return True
#     return False
# print(div(55))
# print(div(33))

# #Pass year and check leap year
# def Year(year):
#     if (year%4==0 and year%100!=0) or year%400==0:
#         return True
#     return False
# print(Year(2024))

# #Pass character and check vowel or consonant
# def voco(char):
#     if char in ("A","E","I","O","U"):
#         print(f"{char} is Vowel")
#     else:
#         print(f"{char} is consonant")
#     return
# print(voco("D"))

# #Perfect Number
# def Perfect(num):
#     Sum=0
#     Diviser=1
#     while Diviser<num:
#         if num%Diviser==0:
#             Sum=Sum+Diviser
#         Diviser+=1
#     if Sum==num:
#         return True
#     return False
# print(Perfect(34))