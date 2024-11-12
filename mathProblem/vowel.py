name=input("Enter the Name ")
vowel='aeiou'
count=0
for i in name.lower() :
    if i in vowel:
     count+=1
    
print(count)