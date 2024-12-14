a={1,2,3,4,5}
print(type(a),a)


# By using Iter object 
iterable=iter(a)
print(*(iterable))

# By using Loop
for i in iterable:
     print(i , end=',')