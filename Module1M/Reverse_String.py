##QUESTION TITLE	Reverse the String
#PROBLEM STATEMENT	Write a Python program to reverse a given string without using any 
# predefined functions. The program should prompt the user to input a string and then 
# output the reversed version of that string.
#CONSTRAINTS	Input:-
#Input Constraints:
#A single word,  containing only alphabetic characters 
#Output:-
#The reverse of the input string 
#PUBLIC TESTCASE	Input:-
#Hello
#Output:- 
#olleH
String=input("Enter The Input: ")
result=""
for i in range(len(String)-1,-1,-1):
    result=result+String[i]
print(result)