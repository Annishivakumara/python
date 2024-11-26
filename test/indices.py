#Problem Statement:
#Write a Python program that extracts and outputs the  characters at odd indices (0-based index) of a given string.
#Input Format Description:
#The first line contains a string, which may consist of letters and other characters.
#Example Input:
#Arijit
#Output Format Description:
#The output should be a string containing the characters at the odd indices (0-based index) of the given string.
#Example Output:
#rjt
#
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