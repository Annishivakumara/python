str1=input("enter the String ")
print(str1)
oddindex=""
evenindex=""
for i in range(1,len(str1)):
    if i%2==1:
       oddindex +=str1[i]
    else:
        evenindex +=str1[i]
print(f"Odd index Values: " ,oddindex)
print(f"Even Index values :",evenindex)