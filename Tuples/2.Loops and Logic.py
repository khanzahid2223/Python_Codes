#16.Print every element of a tuple using a for loop
nums=(1,2,3,4,5,6,7,8,9,10)
for num in nums:
    print(num)

#17.Print every element of a tuple using a while loop
nums=(1,2,3,4,5,6,7,8,9,10)
n=len(nums)
i=0
while i<=n:
    print(i)
    i+=1

#18.Creata a tuple of 5 numbers . Print the first , second and middle one sing index
nums=[1,2,3,4,5]
n=len(nums)
print(f"First={nums[0]}")
print(f"Last={nums[-1]}")
print(f"Middle={nums[n//2]}")