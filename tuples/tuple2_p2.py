#find the maximum number  in the tuple
#$g=(22,34,15,78,1,33,44)
g=tuple(map(int , input("Enter The Number: ").split()))
max_=-1
mini=g[0]

for i in g:
    if  i>max_:
        max_=i
    if i<mini:
           mini=i
print(max_)
print(mini)
