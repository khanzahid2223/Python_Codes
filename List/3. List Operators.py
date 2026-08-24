#56.Concatinate two lists
a=[10,20,30,40,50]
b=[60,70,80,90,100]
print(a+b)

#57.Concatinate three lists
a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=[11,12,13,14,15]
print(a+b+c)

#58.Repeat a list 3 time
a=[10,20,30,40,50]
print(a*3)

#59.Repeat a list 5 time
a=[10,20,30,40,50]
print(a*5)

#60.Check whether two lists are equal
a=[1,2,3,4,5,6] 
b=[1,2,3,4,5,6] 
if a==b:
    print("Tow lists are equal")
else:
    print("Two lists are not equal")

#61.Compare two lists using ==
a=[1,2,3,4,5,6] 
b=[1,2,3,4,5,6] 
print("True" if a==b else "False")

#62.Check whether one list is larger than another
a=[2,5,2,65,4,65,5]
b=[0,2,5,4,5,45,5]
n=len(a)
m=len(b)
print("A is larger the B" if n>=m else "B is larger than A")

#63.Check whether the two list have the same length
a=[1,2,3,4,5]
b=[6,7,8,9]
n=len(a)
m=len(b)
print("Two lists have same length" if n==m else "Two lists are not equal")

#64.Create a list using +
a=[2,4,6,7,8,9]
b=[9,8,6,5,4]
print(a+b)

#65.Create a repeated list using *
a=[10,20,30,40,50]
print(a*4)

#66.Combina two student lists
Student1=["Zahid",21,"Male","Mulbagal"]
Student2=["Khan",19,"Male","Banglore"]
print(Student1+Student2)

#67.Combine two subject list
Sub1=["AI","DSA","Python"]
Sub2=["CNN","DBMS","OS"]
print(Sub1+Sub2)

#68.Create a menu list using list concatination
Food=["Biryani","Pizza","Sandveg","Burger"]
Drinks=["Thums Up","Fanta","String","Mirinda"]
print(Food+Drinks)

#69.create a repeated pattern using list multiplication
a=["*"]
print(a*10)