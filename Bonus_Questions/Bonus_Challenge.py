#My Age Calculations(Age*365)
Age=21
print(f"My Age is {Age} and this is {Age*365} days of my life")

#BMI Calculations(BMI=Weight/(Height**2))
Weight=56
Height=5.1
BMI=Weight/(Height**2)
print(f"My BMI is {BMI} and this is {round(BMI,2)}")

#Electricity Bill Calculations(Bill=Units*Rate)
Units=200
Rate=8
Bill=Units*Rate
print(f"My Electricity Bill is {Bill}")


#Calculate Total Marks
AI=99
DBMA=90
ADA=89
CNN=90
CS=78
Python=100
total=AI+DBMA+ADA+CNN+CS+Python
print(total)


#Calculate Shipping Bill
Shoes=7000
Bag=4500
Total=Shoes+Bag
print(Total)

#GST Calculations
Price=200000
GST=Price*18/100
print(GST)


Year=int(input("Entet Year="))
if(Year%4 == 0 and Year%10 !=0) or (Year%400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")    

