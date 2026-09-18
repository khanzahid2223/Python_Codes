#26.Count how many times "a" occurs in a string.
Name="Zahid Aarosh"
print(Name.lower().count("a"))

#27.Count the occurrences of a particular word.
Word="Python is a best language. Python is easy to learn"
print(Word.count("Python"))

#28.Find the position of a character using find().
Name="Zahid"
print(Name.find("a"))

#29.Replace all spaces with -.
Name="Zahid Khan Arosh"
print(Name.replace(" ","-"))

#30.Replace one word with another word.
Name="Zahid Khan"
print(Name.replace("Khan","Arosh"))

#31.Replace all vowels with *.
A="Zahid Arosh"
Result=""
for ch in A:
    if ch.lower() in "aeiou":
        Result+="*"
    else:
        Result+=ch
print(Result)
    
#32.Split a sentence into words.
Name="Zahid Khan Arosh Furkhan"   
print(Name.split()) 

#33.Join a list of words into a sentence.
Name="Zahid Khan Arosh Furkhan"   
print(Name.split()) 
print(" ".join(Name))

#34.Check whether a string starts with "Hello"
Name="Hell0 World!"
Result=Name[:5]
if Result=="Hello":
    print("Yes")
else:
    print("No")

#35.Check whether a string ends with "Python".
Name="My favourate lenguage is Python"
Result=Name.split()
if Result[4]=="Python":
    print("Yes")
else:
    print("No")

#36.Check whether a string contains only alphabets.
Name="Zahid"
if Name.isalpha():
    print("Yes")
else:
    print("No")

#37.Check whether a string contains only numbers.
num="12345"
if num.isdigit():
    print("Yes")
else:
    print("No")

#38.Check whether a string contains alphabets and numbers only.
Str="Zahid2223"
if Str.isalnum():
    print("Yes")
else:
    print("No")

#39.Check whether a string contains only lowercase letters.
Str="zahid"
if Str.islower():
    print("Yes")
else:
    print("No")

#40.Check whether a string contains only uppercase letters.
Str="ZAHID"
if Str.isupper():
    print("Yes")
else:
    print("No")

#41.Remove all spaces from a string.
Str=" Zahid Khan "
print(Str.strip())

#42.Remove all special characters from a string.
Str="Khanzahid2223@#$%"
Result=""
for ch in Str:
    if ch.isalpha() or ch.isdigit():
        Result+=ch
print(Result)

#43.Replace multiple spaces with a single space.
Str="      Zahid Khan       "
print(Str.strip())

#44.Count the number of words in a sentence.
Word="Hello Zahid. How is your coding joiurney."
Result=Word.split()
Count=0
print(Result)
for i in range(0,len(Result)):
    Count+=1
print(Count)

#45.Find the longest word in a sentence.
Word="Hello Zahid. How is your programming journey. All the best dear future AI engineer"
lst=Word.split()
Longest_Word=""
for ch in lst:
    if len(ch)>=len(Longest_Word):
        Longest_Word=ch
print(Longest_Word)


#46.Find the shortest word in a sentence.
Word="Hello Zahid. How is your programming journey. All the best dear future AI engineer"
lst=Word.split()
Shortest_Word=str("+inf")
for ch in lst:
    if len(ch)<len(Shortest_Word):
        Shortest_Word=ch
print(f"Shortest Word is={Shortest_Word}")

#47.Print each word of a sentence on a separate line.
Word="Hello Zahid. How is your programming journey. All the best dear future AI engineer"
Lst=Word.split()
for ch in Lst:
    print(ch)

#48.Sort words of a sentence alphabetically.
Word="Hello Zahid. How is your programming journey. All the best dear future AI engineer"
lst=sorted(Word.lower().split())
print(lst)

#49.Reverse the order of words in a sentence.
Word="Hello Zahid. How is your programming journey. All the best dear future AI engineer"
Lst=Word.split()
print(" ".join(Lst[::-1]))