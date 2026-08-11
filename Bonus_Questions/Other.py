# #Laep Year
# #A year is a leap year if it is divisible by 4,but not by 100, unless it is also divisble by 400
# Year=int(input("Enter the year:"))
# if((Year%4==0 and Year%100!=0) or (Year%400==0)):
#     print("Leap Year")
# else:
#     print("Not a leap year")

# #Check whether a Alphabet is Vowel or Consonant
# Letter=input("Enter a Alphabet:")
# if Letter in ("A","E","I","O","U"):
#     print("Vowel")
# else:
#     print("Consonent")

# #Login With Three Attempts
# Username=input("Enter the user name:")
# if(Username=="Zahid Khan"):
#     password=input("Enter your password:")
#     if(password==2223):
#         print("Login Successful")
#     else:
#         print("Invalid Password")
# else:
#     print("Invalid User Name")

# #ATM with Balance Check
# Acc_Number=int(input("Enter the Account number:"))
# if(Acc_Number==8147642073):
#     PIN=int(input("Enter PIN:"))
#     if(PIN==2223):
#         Amount=int(input("Enter the Amount to withdraw:"))
#         Balance=25000
#         if(Amount>0 and (Amount<=Balance)):
#             print("Please collect your Amount,Thank You!")
#             print(f"New Balance:{Balance-Amount}")
#         else:
#             print("Insufficient Balance")
#     else:
#         print("Invalid PIN")
# else:
#     print("Invalid Account")


# #ATM Menu
# Acc_Number=int(input("Enter your Account number:"))
# Balance=25000
# if(Acc_Number==8147642073):
#     PIN=int(input("Enter your PIN:"))
#     if(PIN==2223):
#         Choice=int(input("Enter your choice\n1.Check Balance\n2.Withdrae\n3.Deposit\n4.Exit\n"))
#         if(Choice==1):
#             print(f"Balance is:{Balance}")
#         else:
#             if(Choice==2):
#                 Amount=int(input("Enter withdraw amount:"))
#                 if(Amount<=Balance):
#                     print("Collect Cash")
#                     print(f"Balance={Balance-Amount}")
#                 else:
#                     print("Insufficient Balance")
#             else:
#                 if(Choice==3):
#                     Deposit_Amount=int(input("Enter Deposit Amount:"))
#                     print(f"Balance={Balance+Deposit_Amount}")
#                 else:
#                     if(Choice==4):
#                         print("Thank You!")
#                     else:
#                         print("Invalid Option")
#     else:
#         print("Invalid PIN")
# else:
#     print("Invalid Account Number")    

# #Online Food Order System
# print("=======================================================")
# print("==============Welcome To StarZ Restaurant==============")
# print("=======================================================")
# print("Menu")
# print("1.Pizza ₹250\n2.Burger ₹150\n3.Sandwich ₹120")
# Choice=int(input("Select the Food item:"))
# if(Choice==1):
#     Price=250
#     Quantity=int(input("How much quality did u want to order:"))
#     Total=Price*Quantity
#     if(Total>=1000):
#         Discount=Total*10/100
#         print(f"10% Discount on your Purchase is={Discount}")
#         Prime=input("Are you a Prime Member?(Yes/No):")
#         if(Prime=="Yes"):
#             Prime_Discount=(Total-Discount)*5/100
#             print(f"Extra 5% discount:{Prime_Discount}")
#             Total_Discount=Discount+Prime_Discount
#             print(f"Final Bill={Total-Total_Discount}")
#         else:
#             print(f"Final Bill={Total-Discount}")
#     else:
#         Prime=input("Are you a Prime Member?(Yes/No):")
#         if(Prime=="Yes"):
#             Prime_Discount2=Total*5/100
#             print(f"5% prime discount{Prime_Discount2}")
#             print(f"Final Bill={Total-Prime_Discount2}")
#         else:
#             print(f"Total={Total}")
# elif(Choice==2):
#     Price=150
#     Quantity=int(input("How much quality did u want to order:"))
#     Total=Price*Quantity
#     if(Total>=1000):
#         Discount=Total*10/100
#         print(f"10% Discount on your Purchase is={Discount}")
#         Prime=input("Are you a Prime Member?(Yes/No):")
#         if(Prime=="Yes"):
#             Prime_Discount=(Total-Discount)*5/100
#             print(f"Extra 5% discount:{Prime_Discount}")
#             Total_Discount=Discount+Prime_Discount
#             print(f"Final Bill={Total-Total_Discount}")
#         else:
#             print(f"Final Bill={Total-Discount}")
#     else:
#         Prime=input("Are you a Prime Member?(Yes/No):")
#         if(Prime=="Yes"):
#             Prime_Discount2=Total*5/100
#             print(f"5% prime discount{Prime_Discount2}")
#             print(f"Final Bill={Total-Prime_Discount2}")
#         else:
#             print(f"Total={Total}")
# elif(Choice==3):
#     Price=120
#     Quantity=int(input("How much quality did u want to order:"))
#     Total=Price*Quantity
#     if(Total>=1000):
#         Discount=Total*10/100
#         print(f"10% Discount on your Purchase is={Discount}")
#         Prime=input("Are you a Prime Member?(Yes/No):")
#         if(Prime=="Yes"):
#             Prime_Discount=(Total-Discount)*5/100
#             print(f"Extra 5% discount:{Prime_Discount}")
#             Total_Discount=Discount+Prime_Discount
#             print(f"Final Bill={Total-Total_Discount}")
#         else:
#             print(f"Final Bill={Total-Discount}")
#     else:
#         Prime=input("Are you a Prime Member?(Yes/No):")
#         if(Prime=="Yes"):
#             Prime_Discount2=Total*5/100
#             print(f"5% prime discount{Prime_Discount2}")
#             print(f"Final Bill={Total-Prime_Discount2}")
#         else:
#             print(f"Total={Total}")
# else:
#     print("Sorry the Food item you are trying to order is not available,Thank You!")


# #StarZ Shopping Mall
# print("===============================================")
# print("               StarZ Shopping Mall             ")
# print("===============================================")
# print("1.Laptop     ₹50,000\n2.Mobile     ₹20,000\n3.Headphones ₹2,000\n4.Smart Watch ₹5,000")
# print("===============================================")
# Choice=int(input("Which Product do you want to purchase:"))
# if Choice in (1,2,3,4):
#     if(Choice==1):
#         print("Laptop ₹50,000")
#         Price=50000
#     elif(Choice==2):
#         print("Mobile ₹20,000")
#         Price=20000
#     elif(Choice==3):
#         print("Headphones ₹2,000")
#         Price=2000
#     elif(Choice==4):
#         print("Smart Watch ₹5,000")
#         Price=5000
#     Quantity=int(input("How much quantity the product you want:"))
#     Total=Price*Quantity
#     # print(f"Total Bill={Total}")
#     if(Total>=100000):
#         Discount=Total*20/100
#         print(f"20% discount on your purchase,that is:{Discount}")
#         Prime=input("Are you visiting our mall first time(Yes/No):")
#         if(Prime=="Yes"):
#             print(f"There is 5% special discount on your purchase")
#             Prime_Discount=Total*5/100
#             Total_Discount=Discount+Prime_Discount
#             print(f"After 5% special discount your bill is:{Total-Total_Discount}")
#             Coupon=input("Did you have our special coupon:")
#             if(Coupon=="Yes"):
#                 print("There is ₹1000 off on your purchase")
#                 Coupon_Discount=Total-Total_Discount
#                 print(f"Total Bill is:{Coupon_Discount-1000}")
#             # else:
#             #     print(f"Final Bill is:{Total-Total_Discount}")
#         else:
#             print(f"Total Bill={Total-Discount}")
#     else:
#         if(Total>=50000):
#             Discount=Total*10/100
#             print(f"10% discount on your purchase,that is:{Total-Discount}")
#             Coupon=input("Did you have our special coupon:")
#             if(Coupon=="Yes"):
#                 print("There is ₹1000 off on your purchase")
#                 Coupon_Discount=Total-Discount
#                 print(f"Total Bill is:{Coupon_Discount-1000}")
#             else:
#                 print("Invalid Coupon")
#         else:
#             print(f"Finall Bill:{Total}")
# else:
#     print("Invalid Product")