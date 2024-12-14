#my_set=set(map(int , input("Enter The Elements: ").split()))
my_set={22,33, 44, 0,}
while my_set:
    removed_item=my_set.pop()
    print(removed_item,end=',')
    #Removed Statement
print(my_set)