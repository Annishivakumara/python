#print All Upper letter in our String 
name = "SHIVAKUMARA anni"
count=0
for char in name:
    if char.isupper():
        print(f"Upper letter in name {str(char)}")
        count+=1
print(count)