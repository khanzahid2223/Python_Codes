#Calculator using Function
Num1=int(input("Entar a first number:"))
Num2=int(input("Entar a second number:"))
print("1.Addioton\n2.Substraction\n3.Multiplication\n4.Division")
Choice=int(input("Enter your choice:"))
def Add(Num1,Num2):
        Add=Num1+Num2
        return Add

def Sub(Num1,Num2):
        Sub=Num1-Num2
        return Sub

def Mul(Num1,Num2):
        Mul=Num1*Num2
        return Mul

def Div(Num1,Num2):
        Div=Num1/Num2
        return Div

if Choice==1:
    print(Add(Num1,Num2))
elif Choice==2:
    print(Sub(Num1,Num2))
elif Choice==3:
    print(Mul(Num1,Num2))
elif Choice==4:
        if Num2==0:
                print("Division by zero is not possible.")
                quit()
        print(Div(Num1,Num2))
else:
    print("Invalid Choice")

# ATM Machine
Balance = 50000


def Check_Balance(Balance):
    print(f"Current Balance is ₹{Balance}")
    return Balance


def Deposit_Amount(Balance):
    Money = int(input("How much amount you want to deposit:"))
    Balance = Balance + Money
    print("Deposit Successful!")
    print(f"Balance after deposit is ₹{Balance}")
    return Balance


def Wirhdraw_Amount(Balance):
    Money = int(input("How much amount you want to withdraw:"))
    if Money < Balance:
        Balance = Balance - Money
        print("Withdraw Successful!")
        print(f"Balance after withdraw is ₹{Balance}")
    else:
        print("Insufficient Balance")
    return Balance


def Exit():
    return Exit


while True:
    print("*******ATM Menu*******")
    print("1.Check Balance\n2.Deposit Amount\n3.Withdraw Amount\n4.Exit")
    print("***********************")
    Choice = int(input("Enter your choice:"))

    if Choice == 1:
        Check_Balance(Balance)
    elif Choice == 2:
        Balance = Deposit_Amount(Balance)
    elif Choice == 3:
        Balance = Wirhdraw_Amount(Balance)
    elif Choice == 4:
        Exit()
        break
    else:
        print("Invalid Choice")

# Student Management System
Student_Name = "Zahid"
Roll_Number = 205
Age = 21
Course = "AI"
Sub1_Marks = 99
Sub2_Marks = 100
Sub3_Marks = 95


def Add_Student(
    Student_Name, Roll_Number, Age, Course, Sub1_Marks, Sub2_Marks, Sub3_Marks
):
    Name = input("Enter student name:")

    Roll = int(input("Enter Student Roll Number:"))

    age = int(input("Enter Student Age:"))
    Age = age
    course = input("Which Course the student want to persuing:")
    Course = course
    sub1 = int(input("Enter First Subject Marks: "))
    Sub1_Marks = sub1
    sub2 = int(input("Enter Second Subject Marks: "))
    Sub2_Marks = sub2
    sub3 = int(input("Enter Third Subject Marks: "))
    Sub3_Marks = sub3
    print("Student Added Successfully!")
    return Student_Name, Roll_Number, Age, Course, Sub1_Marks, Sub2_Marks, Sub3_Marks


def search_Student(Student_Name):
    Roll = int(input("Enter Student Roll Number:"))
    if Roll == Roll_Number:
        print(
            f"Student Name:{Student_Name}\nRoll Number:{Roll_Number}\nAge:{Age}\nCourse:{Course}\nSub1 Marks:{Sub1_Marks}\nSub2 Marks:{Sub2_Marks}\nSub3 Marks:{Sub3_Marks}"
        )
    else:
        print("Student not found")
    return Student_Name


def Update_Marks(Sub1_Marks, Sub2_Marks, Sub3_Marks):
    Roll = int(input("Enter Student Roll Number:"))
    if Roll == Roll_Number:
        Sub1 = int(input("Enter first subject marks:"))
        Sub1_Marks = Sub1
        Sub2 = int(input("Enter second subject marks:"))
        Sub2_Marks = Sub2
        Sub3 = int(input("Enter third subject marks:"))
        Sub3_Marks = Sub3
        print("Marks Updated Successfully!")
    else:
        print("Student not found")
    return Sub1_Marks, Sub2_Marks, Sub3_Marks


def Delete_Student(
    Student_Name, Roll_Number, Age, Course, Sub1_Marks, Sub2_Marks, Sub3_Marks
):
    Roll = int(input("Enter Student Roll Number:"))
    if Roll == Roll_Number:
        Student_Name = None
        Roll_Number = None
        Age = None
        Course = None
        Sub1_Marks = None
        Sub2_Marks = None
        Sub3_Marks = None
        print(
            f"Student Name:{Student_Name}\nRoll Number:{Roll_Number}\nAge:{Age}\nCourse:{Course}\nSub1 Marks:{Sub1_Marks}\nSub2 Marks:{Sub2_Marks}\nSub3 Marks:{Sub3_Marks}"
        )
    else:
        print("Student not found")
    return Student_Name, Roll_Number, Age, Course, Sub1_Marks, Sub2_Marks, Sub3_Marks


def Calcilate_Result(Sub1_Marks, Sub2_Marks, Sub3_Marks):
    Total = Sub1_Marks + Sub2_Marks + Sub3_Marks
    Avg = Total / 3
    if Avg >= 35:
        print("Pass")
    else:
        print("Fail")
    return Sub1_Marks, Sub2_Marks, Sub3_Marks


def Calculate_Grade(Sub1_Marks, Sub2_Marks, Sub3_Marks):
    Total = Sub1_Marks + Sub2_Marks + Sub3_Marks
    Avg = Total / 3
    if Avg >= 90:
        print("Grade A+")
    elif Avg >= 80 and Avg < 90:
        print("Grade A")
    elif Avg >= 70 and Avg < 80:
        print("Grade B")
    elif Avg >= 60 and Avg < 70:
        print("Grade C")
    elif Avg >= 50 and Avg < 60:
        print("Grade D")
    elif Avg >= 35 and Avg < 50:
        print("Grade E")
    else:
        print("Grade F")
    return Sub1_Marks, Sub2_Marks, Sub3_Marks


def Display_Std_Details(
    Student_Name, Roll_Number, Age, Course, Sub1_Marks, Sub2_Marks, Sub3_Marks
):
    print(
        f"Student Name:{Student_Name}\nRoll Number:{Roll_Number}\nAge:{Age}\nCourse:{Course}\nSub1 Marks:{Sub1_Marks}\nSub2 Marks:{Sub2_Marks}\nSub3 Marks:{Sub3_Marks}"
    )
    return Student_Name, Roll_Number, Age, Course, Sub1_Marks, Sub2_Marks, Sub3_Marks


def exit():
    print("Thank you for using Student Management System.")
    return


while True:
    print("**********Student Management System**********")
    print(
        "1.Add Student\n2.Search Student\n3.Update Marks\n4.Delete Student\n5.Calculate Result\n6.Calculatr Grade\n7.Display Student Details\n8.Exit"
    )
    Choice = int(input("Enter your choice:"))
    if Choice == 1:
        Add = Add_Student(
            Student_Name, Roll_Number, Age, Course, Sub1_Marks, Sub2_Marks, Sub3_Marks
        )
    elif Choice == 2:
        Search = search_Student(Student_Name)
    elif Choice == 3:
        Update = Update_Marks(Sub1_Marks, Sub2_Marks, Sub3_Marks)
    elif Choice == 4:
        Delete = Delete_Student(
            Student_Name, Roll_Number, Age, Course, Sub1_Marks, Sub2_Marks, Sub3_Marks
        )
    elif Choice == 5:
        Result = Calcilate_Result(Sub1_Marks, Sub2_Marks, Sub3_Marks)
    elif Choice == 6:
        Grade = Calculate_Grade(Sub1_Marks, Sub2_Marks, Sub3_Marks)
    elif Choice == 7:
        Display = Display_Std_Details(
            Student_Name, Roll_Number, Age, Course, Sub1_Marks, Sub2_Marks, Sub3_Marks
        )
    elif Choice == 8:
        Exit = exit()
        break
    else:
        print("Invalid Stop")


