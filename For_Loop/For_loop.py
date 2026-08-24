"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()


"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""

for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print()

"""
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
# """
for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(i,end=" ")
    print()

"""
*
* *
* * *
* * * *
* * * * *
"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

"""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""

for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""

for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()

"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()
for i in range(2,6):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()

#Print 1 to 10
for i in range(1,11):
    print(i,end=" ")

# Print 10 to 1
for i in range(10, 0, -1):
    print(i, end=" ")


# Print even numbers from 1 to 100
for i in range(2, 101,2):
        print(i, end=" ")

# Print odd numbers from 1 to 100
for i in range(1, 101,2):
        print(i, end=" ")

# Multiplication Table
Num = int(input("Enter a number:"))
for i in range(1, 11):
    print(f"{Num} x {i} = {Num*i}")

# Find sum of of numbers from 1 to N
Num = int(input("Enter a number:"))
Sum = 0
for i in range(1, Num + 1):
    Sum = Sum + i
print(Sum)

# Find the prodect of numbers from 1 to N(Factorial)
Num = int(input("Enter a number:"))
Fact = 1
for i in range(1, Num + 1):
    Fact = Fact * i
print(Fact)

# Print all multiples of 5 from 1 to 100
for i in range(5, 101,5):
        print(i, end=" ")

# Print number divisible by both 3 and 5
for i in range(15, 201,15):
    print(i, end=" ")

# Print a squares of a number from 1 to 20
Square = 0
for i in range(1, 21):
    Square = i * i
    print(Square, end=" ")

# Count even and odd numbers between 1 to N
N = int(input("Enter a number:"))
Even = 0
Odd = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        Even += 1
    else:
        Odd += 1
print(f"Even Numbers={Even}\nOdd Numbers={Odd}")

#Largest among the numbers
Largest=0
for i in range(1,6):
   Num=int(input("Enter a number:"))
   if(Num>Largest):
      Largest=Num
print(Largest)

#Smallest among the numbers
Smallest=int(input("ENter a number:"))
for i in range(1,6):
    Num=int(input("Enter a number:"))
    if(Num<Smallest):
        Smallest=Num
print(Smallest)

#Sum of even numbers
Sum=0
for i in range(2,21,2):
    Sum=Sum+i
print(Sum)

# Sum of even numbers
Sum = 0
for i in range(1, 22, 2):
    Sum = Sum + i
print(Sum)

# Num divisible by 7 but not 5
for i in range(1, 101):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=" ")

# Count Number divisible by 3 between 1 to N
Count = 0
Num = int(input("Enter a number:"))
for i in range(3, Num + 1, 3):
    Count = Count + 1
print(Count)

# Print numbers not divisible by 2
for i in range(1, 21):
    if i % 2 != 0:
        print(i)

Avg = 0
Sum = 0
for i in range(1, 6):
    Num = int(input("Entar a number:"))
    Sum = Sum + Num
    Avg = Sum / 5
print(Avg)

#Prime Number
Prime=True
Num=int(input("Enter a number:"))
if Num<=1:
    Prime=False
else:
    for i in range(2,Num):
        if Num%i==0:
            Prime=False
            break
if Prime:
    print(f"{Num} is Prime")
else:
    print(f"{Num} is not Prime")

#Number is Palindrome
Rev=0
Num=int(input("Enter a number:"))
Org=Num
Count=len(str(Num))
for i in range(Count):
    LD=Num%10
    Rev=Rev*10+LD
    Num=Num//10
if(Org==Rev):
    print(f"{Org} is Palindrome")
else:
    print(f"{Org} is not Palindrome")

#ArmStrong Number
Num=int(input("Enter a number:")) 
Org=Num
Sum=0
# Count=len(str(Num))
Count=0
Temp=Num
while Temp>0:
    Count+=1
    Temp=Temp//10
    
for i in range(Count):
    LD=Num%10
    Sum=Sum+(LD**Count)
    Num=Num//10
if Org==Sum:
    print(f"{Org} is ArmStrong Number")
else:
    print(f"{Org} is not ArmStrong Number")

#Stop printing number when it reaches to 50
for i in range(1,101):
    if i==50:
        break
    print(i)

#Skip all even numbers using continue
for i in range(1,101):
    if i%2!=0:
        continue
    print(i)

#Skip all multiples of 5
for i in range(1,101):
    if i%5==0:
        continue
    print(i)

#Stop when negative number is entered
for i in range(1,6):
    N=int(input("Enter a number:"))
    if N<0:
        break
    print(N)

#Check a Password with 3 attempts
Pass=2223
for i in range(1,4):
    Num=int(input("Enter your Password:"))
    if Pass==Num:
        print(f"{Num} is Valid Password")
    else:
        print("Invalid Password")
    
