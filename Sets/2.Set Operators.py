#16.Find the union of two sets.
# a={89,98,90,89,32}
# b={89,25,36}
# # print(a | b)
# print(a.union(b))

#17.Find the intersection of two sets.
# a={89,98,90,89,32}
# b={89,25,36}
# print(a & b)
# print(a.intersection(b))

#18.Find the elements present in Set A but not Set B.
# a={1,2,5,3}
# b={5,2,3,6}
# result=set()
# for num in a:
#     if num not in b:
#         result.add(num)
# print(result)

#19.Find the elements present in Set B but not Set A.
# a={10,20,30,40}
# b={50,90,10,20,30,40}
# result=set()
# for num in b:
#     if num not in a:
#         result.add(num)
# print(result)

# #20.Find the symmetric difference between two sets.
# A={1,2,3,4}
# B={3,4,5,6}
# result=set()
# for num in A:
#     if num not in B:
#         result.add(num)

# for num in B:
#     if num not in A:
#         result.add(num)
# print(result)

#21.Check whether two sets are equal.
# A={10,20,30}
# B={10,20,30,90}
# if A==B:
#     print(f"A and B are equal")
# else:
#     print(f"A and B are not equal")

#22.Check whether one set is a subset of another set.
# A={2,1}
# B={1,2,4,5,6}
# sub_set=True
# for num in A:
#     if num not in B:
#         sub_set=False
#         break
# if sub_set:
#     print("A is a sub set of B")
# else:
#     print("A is not a sub set of B")

# #23.Check whether one set is a superset of another set.
# A={1,2,3,4,5,6}
# B={3,0}
# Super_Set=True
# for num in B:
#     if num not in A:
#         Super_Set=False
#         break
# if Super_Set:
#     print("A is a Super set of B")
# else:
#     print("A is not a Super set of B")

#24.Check whether two sets are disjoint.
# A={1,2,9}
# B={4,5,3}
# Disjiont=True
# for num in B:
#     if num in A:
#         Disjiont=False
#         break
# if Disjiont:
#     print("A is Disjoint of B")
# else:
#     print("A is not the Disjoint of B")

#25.Create two sets and perform all major set operations on them
# A={10,20,30}
# B={20,30,60}
# print(f"Union ={A|B}")
# print(f"Intersection={A&B}")