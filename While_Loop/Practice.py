#Multiplication of Tables
Num=int(input("Enter a number="))
i=1
while i<=10:
    print(f"{Num}x{i}={Num*i}")
    i+=1

#Factorial a Number
Num=int(input("Enter a number="))
Fact=1
i=1
while i<=Num:
    Fact=Fact*i
    i+=1
print(f"Factorian of {Num} is {Fact}")

#Count the digits of a number
Num=int(input("Enter a number="))
Count=0
while Num>0:
    Count+=1
    Num=Num//10
print(f"Count of digit for the given number {Num} is {Count}")

#Reverce of a number
Num=int(input("Enter a number="))
Rev=0
while Num>0:
    LD=Num%10
    Rev=Rev*10+LD
    Num=Num//10
print(f"Reverse of a number {Num} is {Rev}")

#Sum of digits
Num=int(input("Enter a number="))
Sum=0
Rev=0
while Num>0:
    LD=Num%10
    Sum=Sum+LD
    Num=Num//10
print(f"Sumof the digits are:{Sum}")

#Palendriom of number
Num=int(input("Enter a number="))
Original=Num
Rev=0
while Num>0:
    LD=Num%10
    Rev=Rev*10+LD
    Num=Num//10
if(Original==Rev):
    print("Palindrome Number")
else:
    print("Not a Palindrome")

#Arm Strong number
Num=int(input("Enter a number="))
Orginal=Num
Sum=0
Count=len(str(Num))
while Num>0:
    Last_Digit=Num%10
    Sum=Sum+(Last_Digit**Count)
    Num=Num//10
if(Orginal==Sum):
    print(f"{Sum} is ArmStrong Number")
else:
    print(f"{Sum} is not a ArmStrong Number")
    
#Strong Number
Num=int(input("Enter a number="))
Original=Num
Sum=0
while Num>0:
    Last_Digit=Num%10
    Temp=Last_Digit
    Fact=1
    while Temp>0:
        Fact=Fact*Temp
        Temp-=1
    Sum=Sum+Fact
    Num=Num//10
if(Original==Sum):
    print(f"{Original} is Strong Number")
else:
    print(f"{Original} is not a Strong Number")
