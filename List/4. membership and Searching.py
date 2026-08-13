#71.Check whether a number exist in a list
# lst=[90,54,32,78,20]
# if 20 in lst:
#     print(True)
# else:
#     print(False)

#72.Check whether a name exist in a list
# name=["Zahid","Sufiyan","Khan","Samaak","Abu"]
# if "Zahid" in name:
#     print(True)
# else:
#     print(False)

#73.Check whether aa character exist in a list
# char=["A","Z","S","D","F"]
# if "Z" in char:
#     print("Z is in a list")
# else:
#     print("Z is not in a list")

#74.Check whether an element does not exist
# lst=[9,4,3,6,8,1,2,9,3]
# if 10 not in lst:
#     print("Elemant is not in a list")
# else:
#     print("Element is in a list")

#75.search for a student name
# Student=["Zahid","Khan","Pathan"]
# Search="Zahid"
# n=len(Student)
# def search_Student(name):
#     for i in range(0,n):
#         if Search==Student[i]:
#             return True
#         return False
# print(search_Student(Student))
    
#76.Search for a prodect in a shopping cart
# lst=["Rice","Shampo","Nirma","Oil"]
# Search="Rice"
# n=len(lst)
# def search(prodect):
#     for i in range(0,n):
#         if Search==lst[i]:
#             return True
# print(search(lst))

#77.Search a particular subject
# Subject=["AI","DBMS","OS","Python"]
# Search="DBMS"
# n=len(Subject)
# def Search_Subjects(Sub):
#     for i in range(0,n):
#         if Search==Subject[i]:
#             return True    
# print(Search_Subjects(Subject))

# #78.Check whether a list contains any negative numbers
# lst=[1,2,-9,8,-5,3]
# n=len(lst)
# for i in range(0,n):
#     if lst[i]<0:
#         print(f"Negative numbers in a list are={lst[i]}")
    
#79.Chack whether a list contains zero
# lst=[9,7,6,4,2,0]
# n=len(lst)
# def zer_num(num):
#     for i in range(0,n):
#         if lst[i]==0:
#             return True
#     return False
# print(zer_num(lst))

#80.Check whether a list contains duplicate elements
# lst = [10, 20, 30, 20, 40]

# duplicate = False

# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] == lst[j]:
#             duplicate = True
#             break

#     if duplicate:
#         break

# if duplicate:
#     print("List contains duplicate elements")
# else:
#     print("List does not contain duplicate elements")

#81.Find wheather a particular number occer more than once
# lst=[9,5,4,3,2,3,5,3,2,6,7,2,2,7,8,2]
# print(lst.count(2))

#82.Counte occrence of a given number
# lst=[10,20,10,30,10,40,10,50]
# Given=10
# Counter=0
# for num in lst:
#     if num==Given:
#         Counter+=1
# print(f"Count={Counter}")

#83.Find the first occurance of an element
# lst=[10,20,30,40,50]
# Given=40
# n=len(lst)
# for i in range(0,n):
#     if Given==lst[i]:
#         print(f"First occurance at ={i}")
#         break

#84.Find the last occurance of an element
# lst=[10,20,40,60,40,20,10,20,40,30]
# n=len(lst)
# Given=20
# for i in range(n-1,-1,-1):
#     if Given==lst[i]:
#         print(f"Last occurance at ={i}")
#         break

# #85.Check wheather the two list contain the common elements
# lst1=[10,20,30,40]
# lst2=[50,60,10,70]
# n=len(lst1)
# m=len(lst2)
# for i in range(0,n):
#     for j in range(0,m):
#         if lst1[i]==lst2[j]:
#             print(f"Common element is ={lst1[i]}")
#             break
#     break    

#86.Find the common element between two lists
# lst1=[10,20,30,40]
# lst2=[50,60,10,70]
# n=len(lst1)
# m=len(lst2)
# for i in range(0,n):
#     for j in range(0,m):
#         if lst1[i]==lst2[j]:
#             print(f"Common Element is = {lst1[i]}")
#             break

