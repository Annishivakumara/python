#Return Element That is Present Exactly in any one of two List and try to give the Diffrence between Two  Sets:
list1=list(map(int , input("Enter the List 1 Element: ").split()))
list2=list(map(int , input("Enter the List 2 Element: ").split()))
set1=set(list1)
set2=set(list2)

print(set1)
print(set2)

print(set1.difference(set2))
print(set2.difference(set1))
