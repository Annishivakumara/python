#Reverse The List from the user input
list1=list(map(int , input("Enter The Number  list: ").split())) # 11 22 34 4 5 
start_index=len(list1)-1
last_index=0
while  start_index>=last_index:
    print(list1[start_index],end=',')
    start_index-=1