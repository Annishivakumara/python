#QUESTION TITLE	Count the Number of Vowels in a String
#PROBLEM STATEMENT	Write a Python program to count the number of vowels in a given string.
#CONSTRAINTS	Input String:
#•	The first line contains a string (1 ≤ length of string ≤ 1000) in which vowels need to be counted. 
#Output:
#•	An integer representing the count of vowels in the string.
#•	Ignore spaces, numbers, and special characters while counting vowels.

#PUBLIC TESTCASE	Sample Input:
#hello world
#Sample output :
#3
String=input("Enter The String: ")
count=0
vowels='aeiou'
for vo in String.lower():
    if vo in vowels:
        count+=1
       # print(vo,end=',')
print(count)
