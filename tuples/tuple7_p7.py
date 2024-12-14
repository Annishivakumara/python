#Add and Display The Unique elemenets  in a tuple
tuples_to_add=[(1,2),(3,4),(1,2),(5,6),(5,6)]
res=set()
for i in tuples_to_add:
    if  i not in res:
      res.add(i)
print(res)

#Count The specific Numbers
z=(33,44,44,55)
print(z.count(44))

#Print Index Values
print(z.index(44))

#Unpack The all The Items 
k,l,*m=(33,44,55,88,99)
print(m)
k,*l=(33,44,55,88,99)
print(l)