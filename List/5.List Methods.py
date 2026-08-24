# 91.Add an element using append()
name=["Zahid","Pathan","Furkhan"]
name.append("Aarosh")
print(name)

#92.Add multiple elements using extend()
lst=[89,98,35,"Khan"]
lst.extend(["Zahid",87,67,True,False])
print(lst)

#93.Insert an element at the begining
lst=[87,78,65,45]
lst.insert(0,"Zahid")
print(lst)

#94.Insert the element at the middle
lst=[10,20,30,40,50,60]
n=len(lst)
mid=n//2
lst.insert(mid,"Khan")
print(lst)

#95.Remove an element using remove()
lst=[90,65,"Khan","Zahid","Pathan"]
lst.remove("Pathan")
print(lst)

#96.Remove the last element using pop()
lst=[10,20,30,40,50,60]
lst.pop()
print(lst)

#97.Remove an element using index
lst=[90,43,56,77,12,34]
lst.pop(2)
print(lst)

#98.Clear all elements
lst=[90,87,56,54,23,21]
lst.clear()
print(lst)

#99.Find the index of an element
lst=[90,44,23,21,45,76]
ans=lst.index(21)
print(ans)

#100.Count occurance of an element
lst = [90, 10, 44, 10, 23, 10, 21, 45, 10, 76, 10]
ans = lst.count(10)
print(ans)

#101.Sort Number ascending
lst=[90,76,1,34,1,56,76]
lst.sort()
print(lst)

#102.Sort Number desending
lst=[90,76,1,34,1,56,76]
lst.sort(reverse=True)
print(lst)

#103.Sort name alphabetically
lst=["Zahid","Khan","Aarosh","Furkhan","Tayab"]
lst.sort()
print(lst)

#104.Reverse a list using list method
lst=["Zahid","Khan","Aarosh","Furkhan","Tayab"]
lst.reverse()
print(lst)

#105.Create a copy of a list
lst=[10,20,30,40,50,60]
lst1=lst.copy()
print(lst1)

#109.Creating a shopping cart using list methods
# Start
#   ↓
# Create empty Cart
#   ↓
# Display Menu
#   ↓
# 1 → Add Product       → append()
# 2 → Add Multiple      → extend()
# 3 → Insert Product    → insert()
# 4 → Remove Product    → remove()
# 5 → Remove Last       → pop()
# 6 → Search Product    → in
# 7 → Count Product     → count()
# 8 → Find Position     → index()
# 9 → Sort Cart         → sort()
# 10 → Reverse Cart     → reverse()
# 11 → Clear Cart       → clear()
# 12 → Display Cart
#   ↓
# Continue / Exit

shopping=[]
shopping.append("Cloths")
shopping.extend(["Rice","Pant","T-Shirt","Laptop","Mobile"])
shopping.insert(0,"Mouse")
shopping.remove("Pant")
shopping.pop()
ans=shopping.index("Cloths")
print(ans)
shopping.sort()
shopping.sort(reverse=True)
shopping.clear()
print(shopping)

#110.Add 5 prodects to a cart
Cart=["Mobile","laptop","Mouse","Keyboard","Charger"]
print(Cart)

#111.Remove a prodect from the cart
Cart=["Mobile","laptop","Mouse","Keyboard","Charger"]
Cart.remove("laptop")
print(Cart)

#112.Update a prodect in a cart
Cart=["Mobile","laptop","Mouse","Keyboard","Charger"]
Cart.append("Pendrive")
print(Cart)

#113.Display the cart in sorted order
Cart=["Mobile","laptop","Mouse","Keyboard","Charger"]
Cart.sort()
print(Cart)

#114.Find the cheapest prodect
Prodect=[10000,90000,9897,5474637,10000,6555,1000]
print(min(Prodect))

#115.Find the Most expensive prodect
Prodect=[10000,90000,9897,5474637,10000,6555,1000]
print(max(Prodect))

#116.Remove duplicate prodect
products = ["Laptop", "Mouse", "Laptop", "Keyboard", "Mouse"]

unique_products = []

for product in products:
    if product not in unique_products:
        unique_products.append(product)

print(unique_products)