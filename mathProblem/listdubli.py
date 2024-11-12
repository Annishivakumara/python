number=list(map(int,input("enter the List items ").split()))
undubli=[]
for i in number:
    if i not in undubli:
        undubli.append(i)
print(undubli)