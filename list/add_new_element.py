list2=list(map(int , input("Enter The List: ").split()))  # 1 2 3 4 
start_index=len(list2)-1# 0->1  1->2 
end_index=0# 3-> 4  , 
new_list=[5] # empty 
while start_index>=end_index:  # 3 >=0
     new_list.append(list2[start_index]) #1 
     start_index-=1
print(new_list)