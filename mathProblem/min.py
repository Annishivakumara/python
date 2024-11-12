lis=list(map(int,input("Enter The Number: ").split()))
min=lis[0]
start_index=1
last_index=len(lis)-1
while start_index<-last_index:
    if lis[start_index]<min:min=lis[start_index]

start_index+=1
print(min)