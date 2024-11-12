name=input("Enter the name ")
start_index=0
end_index=len(name)-1
while end_index>=start_index:
    print(name[end_index],end=',')
    end_index-=1