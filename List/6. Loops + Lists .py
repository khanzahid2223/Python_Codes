# 121.Print all numbers in a list
lst = [10, 20, 30, 40, 50, 60, 70, 80]
n = len(lst)
for i in range(0, n):
    print(lst[i], end=" ")

#122.Print only even numbers
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(lst)
for i in range(0, n):
    if lst[i] % 2 == 0:
        print(lst[i], end=" ")

#123.Print only odd numbers
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(lst)
for i in range(0, n):
    if lst[i] % 2 == 1:
        print(lst[i], end=" ")

#124.Print positive numbers
lst = [1, -2, -3, 4, -5, 6, 7, 8, -9, 10]
n = len(lst)
for i in range(0, n):
    if lst[i] >= 0:
        print(lst[i], end=" ")

#125.Print negative numbers
lst = [1, -2, -3, 4, -5, 6, 7, 8, -9, 10]
n = len(lst)
for i in range(0, n):
    if lst[i] < 0:
        print(lst[i], end=" ")

#126.Count even numbers
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n=len(lst)
Count=0
for i in range(0,n):
    if lst[i]%2==0:
        Count+=1
print(f"Count={Count}")

#127.Count odd numbers
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(lst)
Count = 0
for i in range(0, n):
    if lst[i] % 2 == 1:
        Count += 1
print(f"Count={Count}")

#128.Count positive numbers
lst = [1, -2, -3, 4, -5, 6, 7, 8, -9, 10]
n = len(lst)
Count = 0
for i in range(0, n):
    if lst[i] >= 0:
        Count += 1
print(f"Count={Count}")

#129.Count negative numbers
lst = [1, -2, -3, 4, -5, 6, 7, 8, -9, 10]
n = len(lst)
Count = 0
for i in range(0, n):
    if lst[i] < 0:
        Count += 1
print(f"Count={Count}")

#130.Count Zeros
lst = [1, 0, 2, 3, 5, 0, 4, 3, 0, 0, 8, 0, 9, 20, 0]
n = len(lst)
Count = 0
for i in range(0, n):
    if lst[i] == 0:
        Count += 1
print(f"Count={Count}")

#131.Find the sum of even numbers
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n=len(lst)
Sum=0
for i in range(0,n):
    if lst[i]%2==0:
        Sum=Sum+lst[i]
print(f"Sum of even numbers are ={Sum}")

#132.Find the sum of odd numbers
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(lst)
Sum = 0
for i in range(0, n):
    if lst[i] % 2 == 1:
        Sum = Sum + lst[i]
print(f"Sum od odd numbers ={Sum}")

#133.Find the largest number without using max()
lst = [10, 20, 50, 80, 90, 70, 99, 91, 42, 6, 23, 45]
n = len(lst)
Maxi = float("-inf")
for i in range(0, n):
    if lst[i] > Maxi:
        Maxi = lst[i]
print(f"Maximun is = {Maxi}")

#134.Find the smallest number without using min()
lst=[10,20,50,80,90,70,99,91,42,6,23,45,-89]
n=len(lst)
Mini=float("+inf")
for i in range(0,n):
    if lst[i]<Mini:
        Mini=lst[i]
print(f"Minimum is ={Mini}")

#135.Find the average without using sum()
lst=[10,20,50,45,32,8,92,56]
n=len(lst)
Total=0
for i in range(0,n):
    Total=Total+lst[i]
print(f"Total ={Total}")
print(f"Avg = {Total/n}")

#136.Count number greater than 50
lst=[20,51,56,30,89,47,78,53,52,20,10,50,58,57,79,88]
n=len(lst)
Count=0
for i in range(0,n):
    if lst[i]>50:
        Count+=1
print(f"Numner greater than 50 are = {Count}")

#137.Count number less than 50
lst=[20,51,56,30,89,47,78,53,52,20,10,50,58,57,79,88]
n=len(lst)
Count=0
for i in range(0,n):
    if lst[i]<50:
        Count+=1
print(f"Numner greater than 50 are = {Count}")

name=["Zahid","Suhana","Aarosh","Furkhan"]
Family=["Husband","Wife","Daughter","Son"]
for i,j in zip(name,Family):
    print(i,":",j)

#138.Find the second largest without using max()
#Better Solution
nums=[20,99,50,86,30,87,40,98,50,20]
n=len(nums)
Largest=float("-inf")
Second_Largest=float("-inf")
for i in range(0,n):
    Largest=max(Largest,nums[i])

for i in range(0,n):
    if nums[i]>Second_Largest and nums[i]!=Largest:
        Second_Largest=nums[i]

print(f"Second Largest is ={Second_Largest}")

#Optimal Solution
nums = [20, 99, 50, 86, 30, 87, 40, 98, 50, 20]
n = len(nums)
Largest = float("-inf")
Sec_Largest = float("-inf")
for i in range(0, n):
    if nums[i] > Largest:
        Sec_Largest = Largest
        Largest = nums[i]
    elif nums[i] > Sec_Largest and nums[i] != Largest:
        Sec_Largest = nums[i]
print(f"Second Largest is ={Sec_Largest}")

#139.Find the second sllmallest number
#Better Solution
nums = [20, 99, 50, 86, 30, 87, 40, 98, 50, 10]
n = len(nums)
Smallest = float("+inf")
Sec_Smallest = float("+inf")
for i in range(0, n):
    Smallest = min(Smallest, nums[i])
for i in range(0, n):
    if nums[i] < Sec_Smallest and nums[i] != Smallest:
        Sec_Smallest = nums[i]
print(f"Second Largest is ={Sec_Smallest}")

#Optimal Solution
nums = [20, 99, 50, 86, 30, 87, 40, 98, 50, 10]
n = len(nums)
Smallest = float("+inf")
Sec_Smallest = float("+inf")
for i in range(0, n):
    if nums[i] < Smallest:
        Sec_Smallest = Smallest
        Smallest = nums[i]
    elif nums[i] < Sec_Smallest and nums[i] != Smallest:
        Sec_Smallest = nums[i]
print(f"Second Smallest is ={Sec_Smallest}")

#140.Find all numbers divisible by 5
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for num in nums:
    if num%5==0:
        print(num)

#141.Find all numbers divisible by both 3 and 5
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for num in nums:
    if num%3==0 and num%5==0:
        print(num)

#142.Seperate odd and even numbers
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
Even=[]
Odd=[]
for num in nums:
    if num%2==0:
        Even.append(num)
    elif num%2==1:
        Odd.append(num)
print(f"Even={Even}\nOdd={Odd}")

#143.Seperate positive and negative numbers
nums=[1,-2,3,4,-5,6,-7,8,9,-10,11,-12,13,-14,15]
Positive=[]
Negative=[]
for num in nums:
    if num>0:
        Positive.append(num)
    elif num<0:
        Negative.append(num)
print(f"Positive={Positive}\nNegative={Negative}")

#144.create a list of squares using a loop
Square=[]
for i in range(1,11):
    Square.append(i*i)
print(f"Square is ={Square} ")

#145.Create a list of Cubes using a loop
Cubes=[]
for i in range(1,11):
    Cubes.append(i**3)
print(f"Cubes is ={Cubes}")

#146.Find duplicate elements
nums = [10, 20, 50, 10, 20, 10, 50, 20, 40, 60, 80, 70, 90, 10, 20, 50, 43, 90]
Seen = []
Duplicate = []
for num in nums:
    if num in Seen:
        if num not in Duplicate:
            Duplicate.append(num)
    else:
        Seen.append(num)
print(f"Orginal list={nums}")
print(f"Seen={Seen}")
print(f"Duplicate lsit={Duplicate}")

#147.Find the unique elements
nums = [10, 20, 50, 10, 20, 10, 50, 20, 40, 60, 80, 70, 90, 10, 20, 50, 43, 90]
Unique = []
Count=0
for num in nums:
    if nums.count(num)==1:
        Unique.append(num)
print(f"Uniquse Elements={Unique}")

#148.Reverse a list using a loop
Nums=[1,2,3,4,5,6,7,8,9]
n=len(Nums)
for i in range(n-1,-1,-1):
    print(Nums[i])

