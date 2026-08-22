"""
Check whether a string starts with "Hello".
Check whether a string ends with "Python".
Check whether a string contains only alphabets.
Check whether a string contains only numbers.
Check whether a string contains alphabets and numbers only.
Check whether a string contains only lowercase letters.
Check whether a string contains only uppercase letters.
Remove all spaces from a string.
Remove all special characters from a string.
Replace multiple spaces with a single space.
Count the number of words in a sentence.
Find the longest word in a sentence.
Find the shortest word in a sentence.
Print each word of a sentence on a separate line.
Sort words of a sentence alphabetically.
Reverse the order of words in a sentence.
"""
#26.Count how many times "a" occurs in a string.
# Name="Zahid Aarosh"
# print(Name.lower().count("a"))

#27.Count the occurrences of a particular word.
# Word="Python is a best language. Python is easy to learn"
# print(Word.count("Python"))

#28.Find the position of a character using find().
# Name="Zahid"
# print(Name.find("a"))

#29.Replace all spaces with -.
# Name="Zahid Khan Arosh"
# print(Name.replace(" ","-"))

#30.Replace one word with another word.
# Name="Zahid Khan"
# print(Name.replace("Khan","Arosh"))

#31.Replace all vowels with *.
# A="Zahid Arosh"
# Result=""
# for ch in A:
#     if ch.lower() in "aeiouAEIOU":
#         Result+="*"
#     else:
#         Result+=ch
# print(Result)
    
#32.Split a sentence into words.
# Name="Zahid Khan Arosh Furkhan"   
# print(Name.split()) 

#33.Join a list of words into a sentence.
Name="Zahid Khan Arosh Furkhan"   
print(Name.split()) 
print(" ".join(Name))