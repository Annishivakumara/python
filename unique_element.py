#create a New List That Conatin Uniqueue element  or number 
list3 = list(map(int , input("Enter the List Numbers: ").split()))
unique_list=[]
for i in  list3:
    if i not in unique_list:
        unique_list.append(i)
print(f"Unique Elements List: {unique_list}")
