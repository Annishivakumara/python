#finding the minimum value in the list
numbers=list(map(int , input("Enters  The Numbers List: ").split()))
min_num=numbers[0]  # 11
start_index=0
end_index=len(numbers)-1
while start_index<end_index:
    if numbers[start_index]<min_num:
         min_num=numbers[start_index]
    start_index+=1
print(f"Minimum values in the list:  {min_num}" )
