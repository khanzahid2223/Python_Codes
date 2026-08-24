#21.Print every key using for loop
Student={"Name":"Zahid","Age":21,"Marks":589,"Course":"AI"}
for key in Student.keys():
    print(key)

#22.Print every value using for loop
Student={"Name":"Zahid","Age":21,"Marks":589,"Course":"AI"}
for val in Student.values():
    print(val)

#23.Print evrey key and value together
Student={"Name":"Zahid","Age":21,"Marks":589,"Course":"AI"}
for key,val in Student.items():
    print(f"{key}:{val}")

#24.Print only Students who scored more then 50
Students={
    "Zahid":89,
    "Tayab":90,
    "Aarosh":32,
    "Furkhan":21
}
for key,val in Students.items():
    if val>=50:
        print(f"{key}:{val}")

#25.Print Students who scored less then 40
Students={
    "Zahid":89,
    "Tayab":90,
    "Aarosh":32,
    "Furkhan":21
}
for key,val in Students.items():
    if val<=40:
        print(f"{key}:{val}")

#26.Find the sum of all values in the dictionary
Students={
    "Zahid":89,
    "Tayab":90,
    "Aarosh":32,
    "Furkhan":21
}
Total=0
for val in Students.values():
    Total+=val
print(Total)

#27.Find the averege of all values
Students={
    "Zahid":89,
    "Tayab":90,
    "Aarosh":32,
    "Furkhan":21
}
Total=0
for val in Students.values():
    Total+=val
print(f"Average is:{Total/len(Students)}")

#28.Find the maximun value in a dictionary
Students={
    "Zahid":89,
    "Tayab":90,
    "Aarosh":32,
    "Furkhan":21
}
Maxi=float("-inf")
for val in Students.values():
    if val>Maxi:
        Maxi=val
print(Maxi)

#29.Find the minimun value in a dictionary
Students={
    "Zahid":89,
    "Tayab":90,
    "Aarosh":32,
    "Furkhan":21
}
Mini=float("+inf")
for val in Students.values():
    if val<Mini:
        Mini=val
print(Mini)

#30.Find the key having Maximun value
Students={
    "Zahid":89,
    "Tayab":90,
    "Aarosh":32,
    "Furkhan":21
}
Maxi=float("-inf")
Maxkey=0
for key,val in Students.items():
    if val>Maxi:
        Maxi=val
        Maxkey=key
print(f"{Maxkey}:{Maxi}")

#31.Find the key having the minimum value
Students={
    "Zahid":89,
    "Tayab":90,
    "Aarosh":32,
    "Furkhan":21
}
Minikey=0
Mini=float("+inf")
for key,val in Students.items():
    if val<Mini:
        Mini=val
        Minikey=key
print(f"{Minikey}:{Mini}")

#32.Count how many values are even
Students={
    "Zahid":89,
    "Tayab":90,
    "Aarosh":32,
    "Furkhan":21
}
Count=0
for val in Students.values():
    if val%2==0:
        Count+=1
print(Count)

#33.Count how many values are odd
Students={
    "Zahid":89,
    "Tayab":90,
    "Aarosh":32,
    "Furkhan":21
}
Count=0
for val in Students.values():
    if val%2==1:
        Count+=1
print(Count)

#34.Find the sum of only even numbers
Students={
    "Zahid":89,
    "Tayab":90,
    "Aarosh":32,
    "Furkhan":21
}
Sum=0
for val in Students.values():
    if val%2==0:
        Sum=Sum+val
print(Sum)

#35.Find the sum of only odd numbers
Students={
    "Zahid":89,
    "Tayab":90,
    "Aarosh":32,
    "Furkhan":21
}
Sum=0
for val in Students.values():
    if val%2==1:
        Sum=Sum+val
print(Sum)

#36.Create a new dicionary containing values greater than 50
Students={
    "Zahid":89,
    "Tayab":90,
    "Aarosh":32,
    "Furkhan":21
}
New_Dict={}
for key,val in Students.items():
    if val>50:
        New_Dict.update({key:val})
print(New_Dict)

#37.Creata a new dictionary containing only even values
Students={
    "Zahid":89,
    "Tayab":90,
    "Aarosh":32,
    "Furkhan":21
}
New_Dict={}
for key,val in Students.items():
    if val%2==0:
        New_Dict.update({key:val})
print(New_Dict)

#38.Creata a new dictionary containing only even values
Students={
    "Zahid":89,
    "Tayab":90,
    "Aarosh":32,
    "Furkhan":21
}
New_Dict={}
for key,val in Students.items():
    if val%2==1:
        New_Dict.update({key:val})
print(New_Dict)

#39.multiplay every value in a dictionary by 2
Students={
    "Zahid":89,
    "Tayab":90,
    "Aarosh":32,
    "Furkhan":21
}
for key,val in Students.items():
    val=val*2
    print(f"{key}:{val}")

#40.Replace every value with it squares
Students={
    "Zahid":89,
    "Tayab":90,
    "Aarosh":32,
    "Furkhan":21
}
for key,val in Students.items():
    val=val*val
    print(f"{key}:{val}")