#Square of Even Numbers of from 1 to 10
#Using List  Comprension
numbers=int(input("enter the Numbers: "))
comp=[i**2 for i in range(1,numbers+1) ]
print(f"Even  Numbers Square: {comp} ")
