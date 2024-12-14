#Count Letters in a String
text=input("Enter the text: ")
letters_count={}
for letter in text:
    if letter.isalpha(): # is used to specify the alphbetic or not
        if  letter in letters_count:
            letters_count[letter]+=1
        else:
            letters_count[letter]=1
print("String Letter Count: ")
for letter,count in letters_count.items():
     print(f"{letter} : {count}" , end=',')