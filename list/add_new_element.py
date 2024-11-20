list2=list(map(int , input("Enter The List: ").split()))  # 1 2 3 4 
start_index=0# 0->1  1->2 
end_index=len(list2)-1# 3-> 4  , 
new_list=list(map(int, input("Entr the List  new Values: ").split())) # empty 
while start_index<=end_index:  # 3 >=0
     new_list.append(list2[start_index]) #1 
     start_index+=1
print(new_list)