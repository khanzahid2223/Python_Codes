#1.Create a set containing 5 integers and print it.
My_set={2,8,9,2,7,9,6}
print(My_set)
print(type(My_set))

#2.Create a set containing 5 different fruits.
Fruits={"Apple","Banana","Cherry","Kiwi","Mango"}
print(Fruits)

#3.Create a set from a list containing duplicate values.
lst=[4,3,2,4,5,5,4,3,2,5,6,7,8,9,3,5,4]
print(set(lst))

#4.Find the length of a set.
sett={90,87,43,12,45,78}
print(len(sett))

#5.Check whether a given element exists in a set
nums={9,8,7,4,3,2,1,5,6,7}
ele=int(input("ENter a element:"))
if ele in nums:
    print("Yes")
else:
    print("No")

#6.Add one new element to a set.
nums={8,9,4,3,2}
nums.add(5)
print(nums)

#7.Add multiple elements to a set.
nums={8,5,4,3,2,6}
nums.update((90,89,10,50))
print(nums)

#8.Remove an element using remove().
nums={9,83,5,7,1,3}
nums.remove(83)
print(nums)

#9.Remove an element using discard().
nums={1,2,3,4,5}
nums.discard(5)
print(nums)

#10.Clear all elements from a set.
nums={90,43,56,12,34,89}
nums.clear()
print(nums)

#11.Delete a set completely.
nums={90,87,43,23}
del nums
print(nums)

#12.Create an empty set correctly.
nums=set()
print(nums)
print(type(nums))

#13.Iterate through all elements of a set using a for loop.
nums={10,20,30,40,50,60,70,80,90,100}
for num in nums:
    print(num)

#14.Find the maximum value in a set.
nums={50,56,42,80,90,99,43,12}
print(max(nums))

#15.Find the minimum value in a set
nums={50,56,42,80,90,99,43,12}
print(min(nums))