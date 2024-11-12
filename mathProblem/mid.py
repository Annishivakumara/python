number=int(input("Enter the Number: "))
item=list(map(int , input(" ").split()))
start_index=len(item)-1
end_index=-1
rev_=[]
for i in range(start_index,end_index,-1):
     rev_.append(item[i])
print(rev_)