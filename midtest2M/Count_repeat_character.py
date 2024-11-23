#PROBLEM STATEMENT	Write a Python program that takes a string and a character as input and outputs the number of times the character appears in the string.
#CONSTRAINTS	Input Format Description: 
#The first line contains a string, which is the review or the text. 
#The second line contains a character, which you need to count in the string. 
#Output Format Description: 
#The output will be an integer representing the number of times the given character appears in the string.
#PUBLIC TESTCASE	
# Input:
#Priyanka 
#A
#Output:
#2
#Explanation: The character 'a' appears twice in "Priyanka".
String=input("Enter The Name: ").lower()
character=input("Enter The Character: ").lower()
count=0
for i in String:
    if i ==character:
        count+=1
print(count)