#1.Print a string "Hello Python".
str="Hello World!"
print(str)

#2.Take a string as input and print it.
str=input("Enter your name:")
print(str)

#3.Find the length of a string.
str="Zahid Khan"
print(len(str))

#4.Convert a string to uppercase.
Str="zahid khan"
print(Str)
print(Str.upper())

#5.Convert a string to lowercase.
a="ZAHID KHAN"
print(a.lower())

#6.Convert the first character of a string to uppercase.
a="hello"
print(a.capitalize())

#7.Convert the first character of every word to uppercase.
a="hello zahid bhai how are you"
print(a.title())

#8.Remove leading spaces from a string.
a=" Zahid Khan"
print(a.lstrip())

#9.Remove trailing spaces from a string.
a="Zahid Khan  "
print(a.rstrip())

#10.Remove spaces from both sides of a string.
a="  Zahid  "
print(a.strip())

#11.Check whether a string is empty or not.
a=""
if a=="":
    print("String is empty")
else:
    print("String is not empty")

#12.Access the first character of a string.
a="Zahid"
print(a[0])

#13.Access the last character of a string.
a="Zahid"
print(a[-1])

#14.Print the first 5 characters of a string.
Str="Programming"
print(Str[:6])

#15.Print the last 5 characters of a string.
Str="Programming"
print(Str[-1:-6:-1])

#16.Print a string in reverse.
A="Zahid Khan"
print(A[::-1])

#17.Print every second character of a string.
A="Programming"
print(A[::2])

#18.Print characters at even indexes.
Name="Zahid Khan"
n=len(Name)
for i in range(0,n):
    if i%2==0:
        print(Name[i])

#19.Print characters at odd indexes.
name="Zahid Khan"
n=len(name)
for i in range(0,n):
    if i%2==1:
        print(name[i])

#20.Count the number of characters in a string without using len().
Name="Zahid Khan"
Total=0
for ch in Name:
    Total+=1
print(Total)

#21.Check whether a particular character exists in a string.
Name="Zahid Khan"
if "Z" in Name:
    print(True)
else:
    print(False)

#22.Check whether a particular word exists in a string.
Address="Yeldur Kolar Banglore"
if "Yeldur" in Address:
    print(True)
else:
    print(False)

#23.Compare two strings.
A="Zahid"
B="Zahid"
if A==B:
    print(True)
else:
    print(False)

#24.Concatenate two strings.
A="Zahid"
B="Khan"
print(A+" "+B)

#25.Repeat a string 5 times
A="Khan"
print(A*5)