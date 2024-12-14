 # String Sort Tricks 
a=tuple(input("Enter The String: ").split())
a_z=tuple(sorted(a))
z_a=tuple(sorted(a,reverse=True))
print(a_z)
print(z_a)