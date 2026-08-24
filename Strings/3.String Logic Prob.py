"""
Find the character with the lowest frequency.
Find the first non-repeating character.
Find the first repeating character.
Remove duplicate characters from a string.
Print only duplicate characters.
Print only unique characters.
Find the most frequent word in a sentence.
Find the least frequent word in a sentence.
Count uppercase and lowercase characters separately.
Swap uppercase characters with lowercase characters.
Toggle the case of every character without using swapcase().
Count the number of digits in a string.
Find the sum of all digits present in a string.
Extract all numbers from a string.
Extract all alphabets from a string.
Extract all special characters from a string.
Find the largest number present inside a string
"""

#51.Check whether a string is a palindrome.
def check_palindrome(Str:str):
    Result=Str[::-1].lower()
    if Result==Str.lower():
        return "String is Palindrome"
    return "String is not Palindrome"
print(check_palindrome("Markram"))

#52.Check whether a string is palindrome without using slicing.
def check_palindrome(Str:str):
    Left=0
    Right=len(Str)-1
    while Left<Right:
        if Str[Left].lower() != Str[Right].lower():
            return "String is not Palindrome"
        Left+=1
        Right-=1
    return "String is Palindrome"
Str="markram"
print(check_palindrome(Str))

#53.Reverse a string without using [::-1].
Str="Zahid"
Reverse=""
for ch in range(len(Str)-1,-1,-1):
    Reverse+=Str[ch]
print(Reverse)

#53.Count vowels in a string.
Name="Zaihd Khan"
Count=0
for ch in Name:
    if ch in "aeiouAEIOU":
        Count+=1
print(Count)

#54.Count consonants in a string.
Name="Zahid Khan"
Count=0
for ch in Name:
    if ch not in "aeiouAEIOU":
        Count+=1
print(Count)

#55.Count vowels, consonants, digits and special characters separately.
Word="Hello Zahid. How is your coding journey jaani@#$. 8147642073"
Vowels=0
Consonants=0
Digits=0
Special_Char=0
for ch in Word:
    if ch in "AEIOUaeiou":
        Vowels+=1
    elif ch.isalpha():
        Consonants+=1
    elif ch.isdigit():
        Digits+=1
    elif ch==" ":
        continue
    else:
        Special_Char+=1
print(f"Vowels={Vowels}\nCOnsonents={Consonants}\nDigits={Digits}\nSpecial Characters={Special_Char}")

#56.Find the frequency of every character.
Name="Zahid Khan Zahid Khan"
Freq={}
for ch in Name:
    if ch in Freq:
        Freq[ch]+=1
    else:
        Freq[ch]=1
print(Freq)

#57.Find the character with the highest frequency.
Name="Zahid Khan"
Freq={}