#QUESTION TITLE	Check if a String is an Anagram
#PROBLEM STATEMENT	
# Write a Python program to Check if  the String is an Anagram or not.
#CONSTRAINTS
# The string may contain any characters, including spaces, punctuation, or 
# other non-alphabet symbols.
#PUBLIC TESTCASE	Input:
#"listen"
#"silent"
#Output:
#True
String1= input("Enter The Input: ")
String2=input("Enter the Inout: ")
for i in String1:
    if i ==' ' or i=='"':
        print("Anagaram")
    else:
        print("Not Anagram")