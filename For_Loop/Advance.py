#Student Result Calculator(Tota,Average,Grade)
Name=input("What is your Name:")
Subjects=int(input("Entet number of subjects:"))
Total=0
Fail=False
Highest=0
for i in range(1,Subjects+1):
    Marks=int(input("Entar your Marks:"))
    if Marks<35:
        Fail=True
    if Marks<=100 and Marks>=90:
        Highest=Marks
    Total=Total+Marks
Average=Total/Subjects
print(f"Total Marks={Total}")
print(f"Average={Average}")
print(f"Highest Marks={Highest}")
if Fail==True:
    print("Fail")
elif Average>=90:
    print("Grade A+")
elif Average>=80:
    print("Grade A")
elif Average>=70:
    print("Grade B")
elif Average>=60:
    print("Grade C")
elif Average>=35:
    print("Pass")
else:
    print("Fail")
    

