# 1.Create a list containing 5 integers
# lst=[2,6,7,10,89]
# print(lst)

# 2.Create a list containing 5 names
# names=["Zahid","Khan","Abu","Samaak","Sufiyan"]
# print(names)

# 3.Create a list containing different data types
# lst = [21, "Zahid", 89.0, True, False]
# print(lst)

#4.Create a empty list and add 5 elements
# lst=[]
# lst.append("Zahid")
# lst.append(90)
# lst.append("Khan")
# lst.append(True)
# lst.append(False)
# print(lst)

#5.Find the length of the list
# lst = [21, "Zahid", 89.0, True, False]
# n=len(lst)
# print(n)

#6.Find a max element in a numeric list
# lst=[45,67,90,43,23,54]
# print(max(lst))

#7.Find a min element in a numeric list
# lst=[45,67,90,43,23,54]
# print(min(lst))

#8.Find the sum of all numbers in a list
# lst=[45,67,90,43,23,54]
# print(sum(lst))

#9..Find the average of elements in a list
# lst=[45,67,90,43,23,54]
# total=sum(lst)
# Avg=total/6
# print(Avg)

#10.Count how many elements present in list
# lst=[78,98,35,24,31,56]
# Count=0
# n=len(lst)
# for i in range(0,n):
#     Count+=1
# print(Count)

#11.check whether a list is empty
# lst=[]
# if not lst:
#     print("List is empty")
# else:
#     print("List is not empty")

#12.Create a list of numbers from 1 to 10
# lst=[]
# for i in range(1,11):
#     lst.append(i)
# print(lst)

#13.Create a list of even numbers from 1 to 20
# lst=[]
# for i in range(1,21):
#     if i%2==0:
#         lst.append(i)
# print(lst)

#14.Create a list of odd numbers from 1 to 20
# lst=[]
# for i in range(1,21):
#     if i%2==1:
#         lst.append(i)
# print(lst)

#15.Create a list containing squares of 1 to 10
# lst=[]
# for i in range(1,11):
#     lst.append(i*i)
# print(lst)

#16.Create a list containing cubes of 1 to 10
# lst=[]
# for i in range(1,11):
#     lst.append(i**3)
# print(lst)

#17.Access first element
# lst=[90,98,45,32,67]
# print(lst[0])

#18.Access the last element
# lst=[90,65,34,21,56]
# print(lst[-1])

#19.Access the third element
# lst=[78,32,45,76,12,90,76]
# print(lst[2])

#20.Access the second last element
# lst=[78,54,32,67,98,43,12]
# print(lst[-2])

#21.Change the first element
# lst=[78,43,23,65,78,90]
# lst[0]=90
# print(lst)

#22.Change the last element
# lst=[78,54,33,21,89,90,0]
# lst[-1]=89
# print(lst)

#23.Change the third element
# lst=[78,54,33,21,89,90,0]
# lst[2]=0
# print(lst)

#24.Change multuple elemnts simultaneously
# lst=[89,54,32,46,78,98]
# lst[0]=2
# lst[2]=90
# lst[-1]=21
# print(lst)

#25.Print evert element using list
# lst=[9,10,15,17,19,22,3]
# n=len(lst)
# for i in range(0,n):
#     print(lst[i])

#26.Print every element with its index
# lst=[9,22,10,5,8,7]
# n=len(lst)
# for i in range(0,n):
#     print(f"Index={i}, Value={lst[i]}")

#27.Print element in reverse order
# lst=[2,5,9,8,0,7]
# n=len(lst)
# for i in range(n-1,-1,-1):
#     print(lst[i])

#28.print only elements greater than 50
# lst=[45,90,67,65,78,43,32,12,34]
# n=len(lst)
# for i in range(0,n):
#     if lst[i]>=50:
#         print(lst[i])

#29.Print only elements less than 50
# lst=[90,87,32,12,4,50,43,78,8]
# n=len(lst)
# for i in range(0,n):
#     if lst[i]<=50:
#         print(lst[i])