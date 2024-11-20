list2=list(map(int , input("Enter The List: ").split()))  # 1 2 3 4 
start_index=len(list2)-1
end_index=0
new_list=[5]  
while start_index>=end_index:
     new_list.append(list2[start_index]) 
     start_index-=1
print(new_list)
