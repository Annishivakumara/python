
'''
# Converting Between Tuples and Other Data Types 
my_tuple=tuple(map(int , input("Enter The Tuple Elements: ").split()))
my_list=list(my_tuple)
print(my_tuple)
print(my_list)
  
# List to Tuple: Similarly, you can convert a list into a tuple using tuple(). 
my_list=list(map(int, input("Enter The elemenst").split()))
my_tuple=tuple(my_list)
print(my_tuple)
'''
#String to Tuple: You can convert a string to a tuple of characters. 
my_String=input("Enter The String: ").split()
my_tuple=tuple(my_String)
print(my_tuple)