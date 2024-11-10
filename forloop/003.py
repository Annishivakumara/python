# Reverse the String 
name = input("Enter the Name ")
result=""
for i in range(len(name)-1,-1,-1):
    result+=name[i]
print(f"Revrsed String name : {result}")