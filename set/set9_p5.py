list1=[1,2,3,4,5,6]
list2=[4,5,6,7,8,9]
set1=set(list1)
set2=set(list2)
print(f"Additinal Elements in set1: {set1.difference(set2)}")
print(f"Missing Element in: {set2.difference(set1)}")

