#1.Create a dictionary containing studen name,age and course
Student={"Name":"Zahid","Age":21,"Course":"AI"}
print(Student)

#2.Create dictionary of 5 countries and their capitals
Country={"India":"Delhi","Pakistan":"Islamabad","Japan":"Tokyo","France":"Paris","Canada":"Ottawa"}
print(Country)

#3.Print all keys from the dictionary
Student={"Name":"Zahid","Age":21,"Course":"AI"}
print(Student.keys())

#4.Print all the values from the dictionary
Student={"Name":"Zahid","Age":21,"Course":"AI"}
print(Student.values())

#5.Print all key value pair from a dictionary
Student={"Name":"Zahid","Age":21,"Course":"AI"}
print(Student.items())

#6.Access a particular element using a key
Student={"Name":"Zahid","Age":21,"Course":"AI"}
print(Student["Course"])

#7.Check whether a particular key exist in a dictionary
Student={"Name":"Zahid","Age":21,"Course":"AI"}
if "Name" in Student:
    print("Yes")

#8.Add a new key-value pair for the existing dictionary
Student={"Name":"Zahid","Age":21,"Course":"AI"}
Student.update({"Marks":90,"ID":205})
print(Student)

#9.Delete a particular key from a dictionary
Student={"Name":"Zahid","Age":21,"Course":"AI"}
Student.pop("Course")
print(Student)

#10.Update a value for a exisiting key
Student={"Name":"Zahid","Age":21,"Course":"AI"}
Student["Course"]="Data Sicence"
print(Student)

#11.Find the number of key values in a dictionary
Student={"Name":"Zahid","Age":21,"Course":"AI"}
Count=0
for Key in Student:
    Count+=1
print(Count)

#12.Check whether a dictionary is empty or not
Student={}
if Student=={}:
    print("Yes")
else:
    print("No")

#13.Creata a dictionary using two lists one for keys and one for elements
keys=["Name","Age","City"]
values=["Zahid",21,"Kolar"]
Dictionary=dict(zip(keys,values))
print(Dictionary)

#14.Creata a dictionary containing numbers from 1 to 10 with their squares
Squares={i:i*i for i in range(1,11)}
print(Squares)

#15.Creata a dictionary containing numbers from 1 to 10 with their Cubes
Cubes={i:i**3 for i in range(1,11)}
print(Cubes)

#16.Crata a dictionary of 5  students and their marks
Students={
    "Zahid":[90,98,67],
    "Tayab":[99,90,98],
    "Aarosh":[97,78,98],
    "Furkhan":[90,87,56],
    "Faizal":[98,78,91]
}
print(Students)

#17.Print the marks of particular student
Students={
    "Zahid":[90,98,67],
    "Tayab":[99,90,98],
    "Aarosh":[97,78,98],
    "Furkhan":[90,87,56],
    "Faizal":[98,78,91]
}
print(f"Marks  {Students["Zahid"]}")

#18.Update a marks of a particular student
Students={
    "Zahid":[90,98,67],
    "Tayab":[99,90,98],
    "Aarosh":[97,78,98],
    "Furkhan":[90,87,56],
    "Faizal":[98,78,91]
}
Students["Tayab"]=[100,99,98]
print(Students)

#19.Add a new student and their marks
Students={
    "Zahid":[90,98,67],
    "Tayab":[99,90,98],
    "Aarosh":[97,78,98],
    "Furkhan":[90,87,56],
    "Faizal":[98,78,91]
}
Students["Khan"]=[78,65,45]
print(Students)

#20.Remove the student from the dictionary
Students={
    "Zahid":[90,98,67],
    "Tayab":[99,90,98],
    "Aarosh":[97,78,98],
    "Furkhan":[90,87,56],
    "Faizal":[98,78,91]
}
Students.pop("Faizal")
print(Students)