list1=list(map(int , input("enter The Number: ").split()))
list2=list(map(int , input("Enter The Number: ").split()))

max_list1=list[0]
for num in list1:
    if num > max_list1:
        max_list1=num

max_list2=list[0]
for num1 in list2:
    if num1 > max_list2:
        max_list2=num1

print(max_list1)
print(max_list2)