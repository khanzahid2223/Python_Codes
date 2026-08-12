#31.extract the first 3 elements
# lst=[90,5,43,66,2,7]
# print(lst[0:3])

#32.extract the last 3 elements
# lst=[9,8,4,2,6,7,8,1]
# print(lst[7:4:-1])

#33.Extract the elements from index 2 to 6
# lst=[9,8,4,2,6,7,8,1]
# print(lst[2:])


#34.Extract every second element
# lst=[9,8,4,2,6,7,8,1]
# print(lst[::2])

#35.Extract every 3rd element
# lst=[9,8,4,2,6,7,8,1]
# print(lst[::3])

#36.reverse a list using slicing
# lst=[9,8,4,2,6,7,8,1]
# print(lst[::-1])

#37.Copy a list using slicing
# lst=[9,8,4,2,6,7,8,1]
# copy=lst[::]
# print(f"Orginal List={lst}")
# print(f"Copy List={copy}")

#38.Extract all even index elements
lst=[1,2,3,4,5,6,7,8,9,10]
# n=len(lst)
# for i in range(0,n):
#     if lst[i]%2==0:
#         print(lst[i])

#39.Extract all odd index elements
# lst=[1,2,3,4,5,6,7,8,9,10]
# n=len(lst)
# i=0
# while i<=n-1:
#     if lst[i]%2==1:
#         print(lst[i])
#     i+=1

#40.Print half of the list
# lst=[45,65,23,89,90,21,45,32,67,23,16,86]
# n=len(lst)
# half=n//2
# print(lst[0:half])

#41.Print second half of the list
# lst=[45,65,23,89,90,21,45,32,67,23,16,86]
# n=len(lst)
# half=n//2
# print(lst[half:])

#42.Swap first and lset element
# lst=[10,20,30,40,50,60,70,80,90]
# n=len(lst)
# temp=lst[0]
# lst[0]=lst[n-1]
# lst[n-1]=temp
# print(lst)

#43.Swap second and second last  element
# lst=[10,20,30,40,50,60,70,80,90]
# n=len(lst)
# temp=lst[1]
# lst[1]=lst[n-2]
# lst[n-2]=temp
# print(lst)

#44.Replace the first three elements
# lst=[10,20,30,40,50,60,70,80,90]
# lst[0]=1
# lst[1]=2
# lst[2]=3
# print(lst)

#45.Replace the last two elements
# lst=[10,20,30,40,50,60,70,80,90]
# lst[-1]=1
# lst[-2]=2
# print(lst)

#46.Remove the first element using slicing
# lst=[10,20,30,40,50,60,70,80,90]
# print(lst[1:])

#47.Remove the last element using slicing
# lst=[10,20,30,40,50,60,70,80,90]
# n=len(lst)
# print(lst[:n-1])

#48.Create a new list containing a middle element
# lst=[10,20,30,40,50,60,70,80,90]
# n=len(lst)
# print(f"Middle Element={lst[n//2]}")

#49.Find the middle element of odd length list
# lst=[1,3,5,6,7,8,9]
# n=len(lst)
# print(f"Odd of Middle list={lst[n//2]}")

#50.Find the middle element of even length list
# lst=[1,3,5,6,7,8,9,8]
# n=len(lst)
# print(f"Even of Middle list={lst[n//2]}")

#51.Reverse only a portion of list
# lst=[10,20,30,40,50,60]
# print(lst[5:1:-1])

#52.Extract element in reverse using slicing
# lst=[10,20,30,40,50,60]
# print(lst[::-1])

#53.Print every alternate element from the end
# lst=[2,3,2,8,6,4,9,4,6,4,6,4,6,5]
# print(lst[::-2])

#54.Rotate a list left by one position
# lst=[10,20,30,40,50]
# temp=[lst[0]]
# new=lst[1:]
# print(new+temp)

