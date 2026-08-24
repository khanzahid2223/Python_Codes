#ATM Machine
Acc_Balance=50000
ATM_Running=True
PIN=2223
Card=input("Insert your card:")
if(Card=="Yes"):
    while ATM_Running==True:
        print("==============================")
        print("           ATM Menu           ")
        print("==============================")
        print("1.Check Balance\n2.Deposit Money\n3.Withdraw Money\n4.Exit")
        Choice=int(input("Enter your choice:"))
        if(Choice==1):
            Ent_pin=int(input("Enter your PIN:"))
            if(Ent_pin==PIN):
                print(f"Amount Balance={Acc_Balance}")
            else:
                print("Invalid PIN")
        elif(Choice==2):
            Ent_pin=int(input("Enter your PIN:"))
            if(Ent_pin==PIN):
                Deposit=int(input("Deposit Amount="))
                if(Deposit>0):
                    Balance=Acc_Balance+Deposit
                    Acc_Balance=Balance
                    print(f"Amount Balance={Balance}")
                else:
                    print("Enter Valid Amount")
            else:
                print("Invalid PIN")
        elif(Choice==3):
            Ent_pin=int(input("Enter your PIN:"))
            if(Ent_pin==PIN):
                Withdraw=int(input("Withdraw Amount:"))
                if(Withdraw>0):
                    if(Withdraw<=Acc_Balance):
                        Balance=Acc_Balance-Withdraw
                        Acc_Balance=Balance
                        print(f"Collect Your Cash")
                        print(f"Amount Balance={Balance}")
                    else:
                        print("Innsufficient Balance")
                else:
                    print("Enter valid Amount")
            else:
                print("Invalid PIN")
        elif(Choice==4):
            ATM_Running=False
        else:
            print("Invalid Choice")
    print("Thank You!")
else:
    print("Insert your card")

#Restaurant Billing System
Total_Bill=0
Restaurant=True
while Restaurant==True:
    print("==================================")
    print("          StarZ Restaurant        ")
    print("==================================")
    print("1.Pizza ₹200\n2.Burger ₹150\n3.Biryani ₹250")
    Menu=int(input("What do you want to order:"))
    if(Menu==1):
        print("Pizza")
        Quantity=int(input("How Much Quantity you want to order:"))
        if(Quantity>0):
            Bill=Quantity*200
            Total_Bill=Total_Bill+Bill
        else:
            print("Pleas select the valid quantity")
    elif(Menu==2):
        print("Burger")
        Quantity=int(input("How Much Quantity you want to order:"))
        if(Quantity>0):
            Bill=Quantity*150
            Total_Bill=Total_Bill+Bill
        else:
            print("Pleas select the valid quantity")
    elif(Menu==3):
        print("Biryani")
        Quantity=int(input("How Much Quantity you want to order:"))
        if(Quantity>0):
            Bill=Quantity*250
            Total_Bill=Total_Bill+Bill
        else:
            print("Pleas select the valid quantity")
    elif(Menu==4):
        Restaurant=False
    else:
        print("Invalid Choice")
print(f"Total Bill={Total_Bill}")
print("Thank You!")
    
#Randam Number Game
import random
Secreat_Number=random.randint(1,10)
Game_Running=True
while Game_Running==True:
    Guess_num=int(input("Guess the number:"))
    if(Guess_num==Secreat_Number):
        print("You have guessed the correct number")
        Game_Running=False  
    else:
        if(Guess_num>Secreat_Number):
            print("Too High")
        else:
            print("Too Low")
        print("Try Again")
        
#Password Checker
Password=2223
Attempts=3
while Attempts>0:
    Pass=(int(input("Enter youe password:")))
    if(Password==Pass):
        print("Valid Password")
        Attempts=0
    else:
        print("Invalid Password,Tyr Again")
        Attempts=Attempts-1

#Reverse the number
Num=int(input("Enter a number="))
Rev=0
while Num>0:
    Last_Digit=Num%10
    Rev=Rev*10+Last_Digit
    Num=Num//10
print(f"The reverse of a given number is {Rev}")

#Sum of Alternate digits
Num=int(input("Enter a number:"))
Sum=0
while Num>0:
    Last_Digit=Num%10
    Sum=Sum+Last_Digit
    Num=Num//10
    Num=Num//10
print(f"The sum of Alternate digits are {Sum}")

#Digital Root
Num=int(input("Enter a number:"))
while Num>9:
    Sum=0
    while Num>0:
        LD=Num%10
        Sum=Sum+LD
        Num=Num//10
    Num=Sum
print(f"Digital Root is={Num}")

#Bank Management System
Balance=50000
PIN=2223
Attempts=3
while Attempts>0:
    Pass=int(input("Enter your PIN:"))
    if(Pass==PIN):
        print("Login Successful....")
        while True:
            print("1.Deposit\n2.Withdraw\n3.Check Balance\n4.Change PIN\n5.Exit")
            Choice=int(input("Enter your choice:"))
            if(Choice==1):
                Deposit=int(input("Deposit Amount:"))
                if(Deposit>0):
                    Balance=Balance+Deposit
                    print(f"Available Balance={Balance}")
                else:
                    print("Invalid Amount")
            elif(Choice==2):
                Withdraw=int(input("Enter Amount to Withdraw:"))
                if(Withdraw>0):
                    if(Withdraw<=Balance):
                        Balance=Balance-Withdraw
                        print(f"Available Balance: {Balance}")
                    else:
                        print("Insufficient Balance" )
                else:
                    print("Invalid Amount")
            elif(Choice==3):
                print(f"Available Balance is={Balance}")
            elif(Choice==4):
                Old_PIN=int(input("Enter Your Current PIN:"))
                if(Old_PIN==PIN):
                    New_PIN=int(input("Enter your New PIN:"))
                    PIN=New_PIN
                    print("PIN Changed Successfully....")
                else:
                    print("Invalid PIN")
            elif(Choice==5):
                print("Thank You!")
                break
            else:
                print("Invalid Choice")
        break
    else:
        Attempts-=1
if(Attempts==0):
    print("Account Blocked")

#Student Management System
Student_Name="Zahid"
Student_Age=21
Student_ID=205
Student_Marks=582
Student_Course="Data Science"
System=True
print("*****************************")
print("  Student Management System  ")
print("*****************************")
while True:
    print("1.Add Student\n2.Search Student\n3.Update Marks\n4.Display Student Details\n5.Delete Student\n6.Exit")
    print("*****************************")
    Choice=int(input("Enter your choice:"))
    if(Choice==1):
        print("Add Student")
        SName=input("Enter Student Name:")
        Student_Name=SName
        SAge=int(input("Enter Student Age:"))
        Student_Age=SAge
        SID=int(input("Enter Student ID:"))
        Student_ID=SID
        SMarks=int(input("Enter Student Marks:"))
        Student_Marks=SMarks
        SCourse=input("Enter Student Course:")
        Student_Course=SCourse
        print("*****************************")
        print(f"Student Name:{SName}\nStudent Age:{SAge}\nStudent ID:{SID}\nStudent Marks:{SMarks}\nStudent Course:{SCourse}")
        print("*****************************")
    elif(Choice==2):
        SID=int(input("Enter Student ID:"))
        if(SID==Student_ID):
            print("Student is exist")
            print(f"Student Name:{Student_Name}\nStudent Age:{Student_Age}\nStudent ID:{Student_ID}\nStudent Marks:{Student_Marks}\nStudent Course:{Student_Course}")
        else:
            print("Invalid Student ID")
        print("*****************************")
    elif(Choice==3):
        SID=int(input("Enter Student ID:"))
        if(SID==Student_ID):
            New_Marks=int(input("Update Students Marks:"))
            Student_Marks=New_Marks
            print(f"Updates Marks:{New_Marks}")
        else:
            print("Invalid Student ID")
        print("*****************************")
    elif(Choice==4):
        print(f"Student Name:{Student_Name}\nStudent Age:{Student_Age}\nStudent ID:{Student_ID}\nStudent Marks:{Student_Marks}\nStudent Course:{Student_Course}")
        print("*****************************")
    elif(Choice==5):
        SID=int(input("Enter Student ID:"))
        if(SID==Student_ID):
            Student_ID=None
            Student_Course=None
            Student_Marks=None
            Student_Age=None
            Student_Name=None
            print("Student Details Deleted Successfully...")
        else:
            print("Student not found")
        print("*****************************")
    elif(Choice==6):
        print("Thank You")
        break
    else:
        print("Wrong Choice")
        
#OTP Generator
import random
OTP=" "
Count=4
while Count>0:
    Digit=random.randint(0,4)
    OTP=OTP+str(Digit)
    Count-=1
print(f"Your OTP is:{OTP}")