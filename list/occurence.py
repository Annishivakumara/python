#count the occurence of  Number 
list4= list(map ( int , input("Enter The Number's List: ").split()))
unique_list=[]
start_index=0
end_index=len(list4)-1
for i in list4:
    if i not in unique_list:
        unique_list.append(i)
print(f"unique List : {unique_list}  ")

count=0
target=int(input("Enter The Number: "))
for i in list4:
    if i==target:
        count+=1
print(f"Repeated Number {count}  and The Number Is  : {target} ")