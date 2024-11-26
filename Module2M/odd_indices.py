#QUESTION TITLE	Extract Characters at odd indices.
#PROBLEM STATEMENT	Write a Python program that extracts and outputs the characters at odd indices (0-based index) of a given string.
#CONSTRAINTS	Input Format Description: The first line contains a string, which may consist of letters and other characters. 
#Output Format Description: The output should be a string containing the characters at the odd indices (0-based index) of the given string.
#PUBLIC TESTCASE	Input: Arijit 
#Output: rjt 
#Explanation: The characters at odd indices (0-based index) are "r", "j", and "t".

String=input("Enter The Name:  ")
odd_indices_char=""
for i in range(1,len(String)):
     if i%2==1:
         odd_indices_char+=String[i]
print(odd_indices_char)