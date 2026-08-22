#56.Sraech for a student by name
# Student={"Name":"Zahid","Age":21,"Gander":"Male"}
# print(Student["Name"])

#57.Check whether a studentt has pass or fail
# Student={"Name":"Zahid","Marks":67}
# if Student["Marks"]>=35:
#     print("Pass")
# else:
#     print("Fail")

# #58.Find all students who score above average
# Students={
#     "Zahid":90,
#     "Khan":34,
#     "Tayab":99,
#     "Aarosh":89,
#     "Furkhan":32
# }
# Total=0
# for key,val in Students.items():
#     Total+=val
#     Avg=Total/len(Students)

# for k,v in Students.items():
#     if v>Avg:
#         print(f"{k}:{v}")

#59.Find all students who scored highest marks
# Students={
#     "Zahid":90,
#     "Khan":34,
#     "Tayab":99,
#     "Aarosh":89,
#     "Furkhan":32
# }
# Highest_Marks=0
# for key,val in Students.items():
#     if val>Highest_Marks:
#         Highest_Marks=val
# for key,val in Students.items():
#     if val==Highest_Marks:
#         print(f"{key}:{val}")