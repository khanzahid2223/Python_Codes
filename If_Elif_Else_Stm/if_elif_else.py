# #Grade Calculation
# Marks=int(input("Enter your Marks:"))
# if(Marks>=85):
#     print("A Grade")
# elif(Marks>=65 and Marks<=84):
#     print("B Grade")
# elif(Marks>=45 and Marks<=64):
#     print("C Grade")
# else:
#     print("Fail")

# #Traffic Light
# Traffic_Light=input("What is the Traffic Light Color:")
# if(Traffic_Light=="Red"):
#     print("Stop the Vehicel")
# elif(Traffic_Light=="Green"):
#     print("Move the Vehicel")
# else:
#     print("Wait/Prepare to stop")

# #ATM Menu
# ATM=input("The Card is inserted. What is your requirement:")
# if(ATM=="Withdraw"):
#     print("Pleas collect your amount")
# elif(ATM=="Bal_Enquiry"):
#     print("You can see how much balance is there in your account")
# elif(ATM=="Mini_Stmt"):
#     print("You can collect the Mini Statement Slip")
# else:
#     print("Invalid Option")

# #Month Name
# Month=int(input("Select one option (1-12):"))
# if(Month==1):
#     print("Januar")
# elif(Month==2):
#     print("February")
# elif(Month==3):
#     print("March")
# elif(Month==4):
#     print("April")
# elif(Month==5):
#     print("May")
# elif(Month==6):
#     print("June")
# elif(Month==7):
#     print("July")
# elif(Month==8):
#     print("August")
# elif(Month==9):
#     print("September")
# elif(Month==10):
#     print("October")
# elif(Month==11):
#     print("November")
# elif(Month==12):
#     print("December")
# else:
#     print("Invalid Month")

# #Days of the Week
# Day=int(input("Select the option (1-7):"))
# if(Day==1):
#     print("Sunday")
# elif(Day==2):
#     print("Monday")
# elif(Day==3):
#     print("Tuesday")
# elif(Day==4):
#     print("Wednesday")
# elif(Day==5):
#     print("Thursday")
# elif(Day==6):
#     print("Friday")
# elif(Day==7):
#     print("Saturday")
# else:
#     print("Invalid Day")

# #Largest among the three numbers
# num1=int(input("Enter the first value:"))
# num2=int(input("Enter the second value:"))
# num3=int(input("Enter the third value:"))
# if(num1>num2 and num1>num3):
#     print(f"{num1} is largest ")
# elif(num2>num3):
#     print(f"{num2} is largest")
# else:
#     print(f"{num3} is largest")

# #Smallest among three numbers
# num1=int(input("Enter the first value:"))
# num2=int(input("Enter the second value:"))
# num3=int(input("Enter the third value:"))
# if(num1<num2 and num1<num3):
#     print(f"{num1} is smallest")
# elif(num2<num3):
#     print(f"{num2} is smallest")
# else:
#     print(f"{num3} is smallest")

# #Electricity Bill Category
# print("**********Electricity Bill************")
# Units=int(input("Customer Units :"))
# if(Units>=0 and Units<=100):
#     print(f"Rate   :₹10 per unit")
#     print(f"Total Bill: {Units*10}")
# elif(Units>=101 and Units<=200):
#     print(f"Rate   :₹20 per unit")
#     print(f"Total Bill: {Units*20}")
# elif(Units>=201 and Units<=300):
#     print(f"Rate   :₹30 per unit")
#     print(f"Total Bill: {Units*30}")
# else:
#     print(f"Rate   :₹40 per unit")
#     print(f"Total Bill: {Units*40}")
# print("Thank You!")
# print("************************************")

# #Tax Slab
# print("=============================")
# print("      Income Tax Report      ")
# print("=============================")
# Amount=int(input("Annual Income:"))
# if(Amount>0 and Amount<=300000):
#     print("No Tax Applied")
# elif(Amount>300000 and Amount<=700000):
#     print(f"Tax Rate: 5%\nTax Amount: {Amount*5/100}\nStatus:Tax Applied")
# elif(Amount>700000 and Amount<=1200000):
#     print(f"Tax Rate: 10%\nTax Amount: {Amount*10/100}\nStatus:Tax Applied")
# elif(Amount>1200000):
#     print(f"Tax Rate: 20%\nTax Amount: {Amount*20/100}\nStatus:Tax Applied")
# else:
#     print("Invalid Income! Please enter a positive amount")
# print("=============================")
# print("     Thank You!     ")
# print("=============================")

# #Empolyee Bonus
# Experience=int(input("How many years of experience you have:"))
# if(Experience>=0 and Experience<2):
#     print("Your experience is less then 2 years so there is no bonus for you,Thank You!")
# elif(Experience>=2 and Experience<5):
#     print(f"You have experience of more than 2 years,your bonus amount is:{Experience*2000}")
# elif(Experience>=5):
#     print(f"You have experience of more than 5 years,your bonus amount is:{Experience*5000}")
# else:
#     print("Pleas enter a valid number,Thank You!")

# #Student Division
# Marks=int(input("Enter your marks:"))
# if(Marks<=100 and Marks>=85):
#     print("Distintion!")
# elif(Marks<=84 and Marks>=65):
#     print("Frst Class")
# elif(Marks<=64 and Marks>=50):
#     print("Second Class")
# elif(Marks<=49 and Marks>=35):
#     print("Pass")
# elif(Marks<=35):
#     print("Fail")
# else:
#     print("Invalid Marks")

# #Cricket Score Category
# Score=int(input("How much score did a player scored:"))
# if(Score==0):
#     print("Duck Out")
# elif(Score>0 and Score<=49):
#     print("Normal Score")
# elif(Score>=50 and Score<=99):
#     print("Half Century")
# elif(Score>=100):
#     print("Century!")
# else:
#     print("Invalid Score")

# #Weather Condition
# Temperature=int(input("What is the current Tempereture:"))
# if(Temperature<=20):
#     print("Cold")
# elif(Temperature>20 and Temperature<=30):
#     print("Pleasent")
# elif(Temperature>30):
#     print("Hot")

# #BMI
# Weight=int(input("What is your Weight:"))
# Height=float(input("What is your Height:"))
# BMI=Weight/(Height**2)
# if(BMI>=0 and BMI<=18.5):
#     print("Underweight")
# elif(BMI>18.5 and BMI<=24.9):
#     print("Normal")
# elif(BMI>24.9 and BMI<=29.9):
#     print("Overweight")
# elif(BMI>29.9):
#     print("Obese")
# else:
#     print("Your Weight and Height is not valid")

# #Ticket Price Catagory
# Amount=int(input("Pay the amount to get a movie ticket:"))
# if(Amount>0 and Amount<100):
#     print("Ticket price is Cheap")
# elif(Amount>=100 and Amount<500):
#     print("Ticket price is medium ")
# elif(Amount>=500):
#     print("Ticket price is more expencive")
# else:
#     print("Invalid Amount")

# #Bank Interest Catagory
# Amount=int(input("Deposit Amount:"))
# Acc_Type=int(input("Select the option\n1-Savings Account\n2-Fixed Deposit\n3-Senior Citizen FD:"))
# if(Acc_Type==1):
#     print("Low Interest")
# elif(Acc_Type==2):
#     print("Medium Interest")
# elif(Acc_Type==3):
#     print("High Interest")
# else:
#     print("Select the Valid Option")

# #Shopping Discount
# Amount=int(input("How much did you purchased:"))
# if(Amount>=0 and Amount<1000):
#     print("Sorry,there is no discount")
# elif(Amount>=1000 and Amount<=4999):
#     print("10% discount on your purchase")
# elif(Amount>=5000 and Amount<=9999):
#     print("20% discount on your purchase")
# elif(Amount>=10000):
#     print("30% discount on your purchase")
# else:
#     print("Please purchase first for discount,Thank You!")

# #Mobile Battery Percentage
# Battery=int(input("What is the battery percentage of your mobile:"))
# if(Battery>=0 and Battery<20):
#     print("Your Battery is low pleas charge immideatly")
# elif(Battery>=20 and Battery<50):
#     print("Battery is at medium level")
# elif(Battery>=50 and Battery<=100):
#     print("You have good battery,You can easily use your mobile")
# else:
#     print("Your Battery should be in the range between 0-100")

# #Internet Speed Catagory
# Speed=int(input("What is your Internet speed:"))
# if(Speed>=0 and Speed<10):
#     print("Internet is Slow")
# elif(Speed>=10 and Speed<=50):
#     print("Internet speed is average")
# elif(Speed>50):
#     print("Your Internet speed is very high")
# else:
#     print("Your Mobile has no internet connection")

# #Tempereture Catagory
# Tempereture=int(input("What is your current Tempereture:"))
# if(Tempereture<0):
#     print("Its Freezing")
# elif(Tempereture>=0 and Tempereture<=15):
#     print("Its Cold")
# elif(Tempereture>16 and Tempereture<30):
#     print("Normal temperature")
# else:
#     print("Temperature is very hot")

# #Exam Rank
# Rank=int(input("Enter your Rank:"))
# if(Rank==1):
#     print("Gold Medalist")
# elif(Rank>1 and Rank<=10):
#     print("Top Performer")
# elif(Rank>=11 and Rank<=100):
#     print("Good Rank")
# elif(Rank>100):
#     print("Needs Improvement")
# else:
#     print("Sorry You are not in the Rank list")

# #Age Group
# Age=int(input("Enter your Age:"))
# if(Age>=0 and Age<=12):
#     print("Child")
#     print("Your Senior Citizen,not eligible for Bolld Donation")
# else:
#     print(f"Invalid Age or Weight  ")