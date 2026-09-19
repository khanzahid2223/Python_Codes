#Sort dictionary by its keys in ascending order
Student={"Name":"Zahid","Age":21,"Marks":590,"Gender":"Male"}
ans=dict(sorted(Student.items(),key=lambda x:x[0]))
print(ans)

#Sort dictionary by its keys in ascending order
Student={"Name":"Zahid","Age":21,"Marks":590,"Gender":"Male"}
ans=dict(sorted(Student.items(),key=lambda x:x[0] ,reverse=True))
print(ans)

#Sort a dict by its value in asscending order
Marks={"AI":99,"DBMS":67,"ADA":35,"Python":91,"Java":54}
ans=dict(sorted(Marks.items(),key=lambda x:x[1]))
print(ans)

#Sort a dict by its value in descending order
Marks={"AI":99,"DBMS":67,"ADA":35,"Python":91,"Java":54}
ans=dict(sorted(Marks.items(),key=lambda x:x[1],reverse=True))
print(ans)

#Find top 3 students based on marks
Marks={"AI":99,"DBMS":67,"ADA":35,"Python":91,"Java":54}
ans=dict(sorted(Marks.items(),key=lambda x:x[1],reverse=True)[:3])
print(ans)

#Find the bottom 3 students based on the marks
Marks={"AI":99,"DBMS":67,"ADA":35,"Python":91,"Java":54}
answer=dict(sorted(Marks.items(),key=lambda x:x[1],reverse=True)[:-4:-1])
print(answer)

#Sort prodect according to their price
Prodect={"Mobile":15000,"Laptop":30000,"Tablet":12000,"Charger":250,"Headset":1000}
ans=dict(sorted(Prodect.items(),key=lambda x:x[1]))
print(ans)

#Sort prodect according to their price from highest to lowest
Prodect={"Mobile":15000,"Laptop":30000,"Tablet":12000,"Charger":250,"Headset":1000}
ans=dict(sorted(Prodect.items(),key=lambda x:x[1],reverse=True))
print(ans)

# #Sort a dictionary containing word frequncy counts from highest frequency to lowest
Prodect={"Mobile":15000,"Laptop":30000,"Tablet":12000,"Charger":250,"Headset":1000}
ans=dict(sorted(Prodect.items(),key=lambda x:x[1],reverse=True))
print(ans)

#Sort characters according to their frequency
Prodect={"Mobile":15000,"Laptop":30000,"Tablet":12000,"Charger":250,"Headset":1000}
ans=dict(sorted(Prodect.items(),key=lambda x:x[1],reverse=True))
print(ans)