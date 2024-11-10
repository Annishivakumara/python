#  Numer of Vowels in the String 
name = input("Enter the Name:  ")
count=0
Vowels = "aeiou"
for i in name :
    if i in Vowels:
        count+=1
print(f"Number of vowels present {count} ")
